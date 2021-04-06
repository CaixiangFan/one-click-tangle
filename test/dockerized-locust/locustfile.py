from iota import Iota, ProposedTransaction, Address, TryteString, TransactionTrytes
from locust import User, task, between, HttpUser, LoadTestShape
import time, json, sys


class IotaClient():
    """
    Simple, sample XML RPC client implementation that wraps iota.Iota and
    fires locust events on request_success and request_failure, so that all requests
    gets tracked in locust's statistics.
    """

    def __init__(self, host):
        self._locust_environment = None
        self.api = Iota(host, testnet = True)

    def __getattr__(self, name):
        func = self.api.__getattribute__(name)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            try:
                result = func(*args, **kwargs)
            except TimeoutError as e:
                total_time = int((time.time() - start_time) * 1000)
                self._locust_environment.events.request_failure.fire(
                    request_type="send", name=name, response_time=total_time, exception=e
                )
            else:
                total_time = int((time.time() - start_time) * 1000)
                self._locust_environment.events.request_success.fire(
                    request_type="send", name=name, response_time=total_time, response_length=sys.getsizeof(result)
                )
                # In this example, I've hardcoded response_length=0. If we would want the response length to be
                # reported correctly in the statistics, we would probably need to hook in at a lower level

        return wrapper


class IotaUser(User):
    abstract = True
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = IotaClient(self.host)
        self.client._locust_environment = self.environment


class IotaApiUser(IotaUser):
    wait_time = between(0,1)
    address = 'ZLGVEQ9JUZZWCZXLWVNTHBDX9G9KZTJP9VEERIIFHY9SIQKYBVAHIMLHXPQVE9IXFDDXNHQINXJDRPFDXNYVAPLZAW'
    message = TryteString.from_unicode('Hello world')
    tx = ProposedTransaction(
        address = Address(address),
        message = message,
        value = 0
    )

    @task
    def send_msg(self):
        result = self.client.send_transfer(transfers = [self.tx])

    @task
    def prepare_transfer(self):
        tx_trytes = self.client.prepare_transfer(transfers=[self.tx])

    @task
    def send_trytes(self):
        api = Iota(adapter="http://localhost:14265", testnet = True)
        tx_trytes = api.prepare_transfer(transfers=[self.tx])
        resp_sendTrytes = self.client.send_trytes(trytes=tx_trytes['trytes'])


class IotaHttpUser(HttpUser):
    headers = {
        'content-type': 'application/json',
        'X-IOTA-API-Version': '1'
    }
    wait_time = between(0,1)

    def stringify(self, command):
        return json.dumps(command).encode("utf-8")
    
    @task
    def ts_pow_broadcast(self):
        # select two tips to attach new transaction
        command_ts = {
            "command": "getTransactionsToApprove"
        }
        request_ts = self.client.request(method='post', name='select_tips', url=self.host, 
                                    data=self.stringify(command_ts), headers=self.headers)
        jsonData = request_ts.json()
        # print(jsonData)
        # propose a transaction and input trytes string to "trytes"
        message = TryteString.from_unicode('Hello world')
        trytes = TransactionTrytes(message)
        command_pow = { 
            "command": "attachToTangle", 
            "trunkTransaction": jsonData['trunkTransaction'],
            "branchTransaction": jsonData['branchTransaction'],
            "trytes": [str(trytes)]
        }
        request_pow = self.client.request(method='post', name='pow', url=self.host, 
                                    data=self.stringify(command_pow), headers=self.headers)
        # print(request_pow.json())
        # broadcast tx with nonce to neighbors, and store to the local ledger
        command_broadcast = {
            "command": "broadcastTransactions",
            "trytes": request_pow.json()['trytes']
        }
        request_broadcast = self.client.request(method='post', name='broadcast', url=self.host, 
                                    data=self.stringify(command_broadcast), headers=self.headers)
        # print(request_broadcast.json())

    @task(0)
    def query_balance(self):
        address = "EC9FPVIROHPHYFUZQPLYTKKEYYRAKEBPGBCZYQUUWYDAIBYOXXZYSNEDXXHBIGXKXPSTDOSTD9PVRTLRD"
        command = {
            "command": "getBalances",
            "addresses": [address]
        }
        request = self.client.request(method='post', name='get_balances', url=self.host, 
                                    data=self.stringify(command), headers=self.headers)
        print(request.json())


class StagesShape(LoadTestShape):
    """
    A simply load test shape class that has different user and spawn_rate at
    different stages.
    Keyword arguments:
        stages -- A list of dicts, each representing a stage with the following keys:
            duration -- When this many seconds pass the test is advanced to the next stage
            users -- Total user count
            spawn_rate -- Number of users to start/stop per second
            stop -- A boolean that can stop that test at a specific stage
        stop_at_end -- Can be set to stop once all stages have run.
    """

    stages = [
        # {"duration": d, "users": 10, "spawn_rate": 10},
        {"duration": 120, "users": 20, "spawn_rate": 50},
        {"duration": 240, "users": 30, "spawn_rate": 50},
        {"duration": 360, "users": 40, "spawn_rate": 50},
        {"duration": 480, "users": 50, "spawn_rate": 50},
        {"duration": 600, "users": 60, "spawn_rate": 100},
        {"duration": 720, "users": 70, "spawn_rate": 100},
        {"duration": 840, "users": 80, "spawn_rate": 100},
        {"duration": 960, "users": 90, "spawn_rate": 100},
        {"duration": 1080, "users": 100, "spawn_rate": 100},
    ]

    def tick(self):
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data
        return None