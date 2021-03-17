from iota import Iota, ProposedTransaction, Address, TryteString
from locust import User, task, between
import time


class IotaClient():
    def __init__(self, host):
        _locust_environment = None
        self.api = Iota(host, testnet = True) 

    def send_transfer(self, *args, **kwargs):
        return self.api.send_transfer(*args, **kwargs)


class IotaRpcClient(IotaClient):
    """
    Simple, sample XML RPC client implementation that wraps xmlrpclib.ServerProxy and
    fires locust events on request_success and request_failure, so that all requests
    gets tracked in locust's statistics.
    """

    _locust_environment = None

    def getattr(self, name):
        func = IotaClient.__getattribute__(self, name)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            try:
                result = func(*args, **kwargs)
            except TimeoutError as e:
                total_time = int((time.time() - start_time) * 1000)
                self._locust_environment.events.request_failure.fire(
                    request_type="iota_send_transfer", name=name, response_time=total_time, exception=e
                )
            else:
                total_time = int((time.time() - start_time) * 1000)
                self._locust_environment.events.request_success.fire(
                    request_type="iota_send_transfer", name=name, response_time=total_time, response_length=0
                )
                # print("total_time: ",total_time)
                # In this example, I've hardcoded response_length=0. If we would want the response length to be
                # reported correctly in the statistics, we would probably need to hook in at a lower level

        return wrapper


class IotaUser(User):
    abstract = True
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = IotaRpcClient(self.host)
        self.client._locust_environment = self.environment


class ApiUser(IotaUser):
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
        # result = self.client.send_transfer(transfers = [tx])
        result = self.client.getattr('send_transfer')(transfers = [tx])
        # print(result['bundle'].tail_transaction.hash)