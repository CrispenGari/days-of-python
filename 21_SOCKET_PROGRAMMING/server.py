
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