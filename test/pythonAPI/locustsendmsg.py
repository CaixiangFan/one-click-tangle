from iota import Iota, ProposedTransaction, Address, Tag, TryteString
from locust import User, task, between, events
import sys, time, json


class QuickStartUser(User):
    wait_time = between(1,3)
    @task
    def send_msg(self):
        with open('config.json', 'r') as f:
            data = json.load(f)
            url = data['url']
        # returns JSON object as a dictionary 
        api = Iota(url, testnet = True) 
        address = 'ZLGVEQ9JUZZWCZXLWVNTHBDX9G9KZTJP9VEERIIFHY9SIQKYBVAHIMLHXPQVE9IXFDDXNHQINXJDRPFDXNYVAPLZAW'
        message = TryteString.from_unicode('Hello world')
        tx = ProposedTransaction(
            address = Address(address),
            message = message,
            value = 0
        )
        # num = 10
        # if len(sys.argv) == 2:
        #     num = int(sys.argv[1])
        # for i in range(num):
        result = api.send_transfer(transfers = [tx], depth=3, min_weight_magnitude=9)
        print(result['bundle'].tail_transaction.hash)

    @events.test_start.add_listener
    def on_test_start(environment, **kwargs):
        print("A new test is starting")

    @events.test_stop.add_listener
    def on_test_stop(environment, **kwargs):
        print("A new test is ending")

