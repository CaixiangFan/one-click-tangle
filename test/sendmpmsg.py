
from multiprocessing import Process
from iota import Iota, ProposedTransaction, Address, Tag, TryteString
import sys
import json

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

def request(num=10):
    for i in range(num):
        result = api.send_transfer(transfers = [tx])
        print(result['bundle'].tail_transaction.hash)

if __name__ == "__main__":  # confirms that the code is under main function
    numproc = 1
    numtx = 10
    if len(sys.argv) == 3:
        numproc = int(sys.argv[1])
        numtx = int(sys.argv[2])

    procs = []

    # instantiating process with arguments
    for i in range(numproc):
        # print(name)
        proc = Process(target=request, args=(numtx,))
        procs.append(proc)
        proc.start()

    # complete the processes
    for proc in procs:
        proc.join()