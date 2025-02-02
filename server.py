import zmq

context = zmq.Context()
sock = context.socket(zmq.PULL)
sock.connect("tcp://127.0.0.1:5690")

while True:
    message = sock.recv()
    print(f"Received: {message.decode()}")