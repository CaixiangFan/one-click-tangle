from iota import Iota, ProposedTransaction, Address, TryteString, TransactionTrytes
from locust import User, task, between, HttpUser
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
                # print(result['bundle'].tail_transaction.hash)
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
    @task
    def send_msg(self):
        address = 'ZLGVEQ9JUZZWCZXLWVNTHBDX9G9KZTJP9VEERIIFHY9SIQKYBVAHIMLHXPQVE9IXFDDXNHQINXJDRPFDXNYVAPLZAW'
        message = TryteString.from_unicode('Hello world')
        tx = ProposedTransaction(
            address = Address(address),
            message = message,
            value = 0
        )
        result = self.client.send_transfer(transfers = [tx])


class IotaHttpUser(HttpUser):
    headers = {
        'content-type': 'application/json',
        'X-IOTA-API-Version': '1'
    }
    wait_time = between(0,1)

    def stringify(self, command):
        return json.dumps(command).encode("utf-8")

    @task
    def query_balance(self):
        address = "EC9FPVIROHPHYFUZQPLYTKKEYYRAKEBPGBCZYQUUWYDAIBYOXXZYSNEDXXHBIGXKXPSTDOSTD9PVRTLRD"
        command = {
            "command": "getBalances",
            "addresses": [address]
        }
        request = self.client.request(method='post', name='get_balances', url=self.host, 
                                    data=self.stringify(command), headers=self.headers)
        print(request.json())

    @task(0)
    def select_tip(self):
        command = {
            "command": "getTransactionsToApprove"
        }
        request = self.client.request(method='post', name='select_tips', url=self.host, 
                                    data=self.stringify(command), headers=self.headers)
        print(request.json())
    
    @task
    def ts_pow_broadcast(self):
        # select two tips to attach new transaction
        command_ts = {
            "command": "getTransactionsToApprove"
        }
        request_ts = self.client.request(method='post', name='select_tips', url=self.host, 
                                    data=self.stringify(command_ts), headers=self.headers)
        jsonData = request_ts.json()
        print(jsonData)
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
        print(request_pow.json())
        # broadcast tx with nonce to neighbors, and store to the local ledger
        command_broadcast = {
            "command": "broadcastTransactions",
            "trytes": request_pow.json()['trytes']
        }
        request_broadcast = self.client.request(method='post', name='broadcast', url=self.host, 
                                    data=self.stringify(command_broadcast), headers=self.headers)
        print(request_broadcast.json())