import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect('tcp://10.2.9.136:5556')
socket.subscribe('tx')
print ("Socket connected")

while True:
    print ("Waiting for events from the node")
    message = socket.recv()
    data = message.split()
    print ("Transaction confirmed by milestone index: ", data[1])
    print ("Transaction hash: ", data[2])