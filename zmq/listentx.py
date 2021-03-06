import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.SUB)
# socket.connect('tcp://10.2.9.136:5556')
socket.connect('tcp://zmq.devnet.iota.org:5556')
socket.subscribe('tx')
socket.subscribe('sn')
print ("Socket connected")

while True:
    print ("Waiting for events from the node")
    message = socket.recv()
    print(message)
    # data = message.split()
    # print ("Transaction confirmed by milestone index: ", data[1])
    # print ("Transaction hash: ", data[2])