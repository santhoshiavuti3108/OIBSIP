import socket
import threading

HOST = "127.0.0.1"
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

print("Server started...")

def broadcast(message, client):
    for c in clients:
        if c != client:
            c.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            if not message:
                break
            broadcast(message, client)
        except:
            break

    clients.remove(client)
    client.close()

while True:
    client, addr = server.accept()
    print(f"Connected: {addr}")
    clients.append(client)
    threading.Thread(target=handle, args=(client,)).start()
    