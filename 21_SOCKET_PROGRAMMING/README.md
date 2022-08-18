### Socket programming.

In this practical we are going to have a look at how we can create a socket server that allows communication between the server and the client.

1. server code

```py


import socket
from threading import Thread, active_count
from requests import get

PUBLIC = False

HEADER = 64
PORT = 5050
IP_ADDRESS = get('https://api.ipify.org').content.decode('utf8') if PUBLIC else socket.gethostbyname(socket.gethostname())
ADDR = (IP_ADDRESS, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            # sending the message to the client
            conn.send("Msg received".encode(FORMAT))
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {IP_ADDRESS}")
    while True:
        conn, addr = server.accept()
        thread = Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {active_count() - 1}")

print("[STARTING] server is starting...")
start()
```

2. client code

```py

import socket
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    # recieving messages from the server
    print(client.recv(2048).decode(FORMAT))

while True:
    message = input("ENTER A MESSAGE OR (q) to quit: \n").strip()
    if message.lower() == 'q':
        break
    send(message)

send(DISCONNECT_MESSAGE)
```

You can test the communication by running these two files. First run the server.py file as follows:

```shell
python server.py
```

You can start the client by running the following command:

```shell
python client.py
```

> Note that if you are getting an error when running the client, you may want to disable firewall on your windows computer.
