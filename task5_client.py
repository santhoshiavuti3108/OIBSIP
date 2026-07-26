import socket
import threading

HOST = "127.0.0.1"
PORT = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

name = input("Enter your name: ")

def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            print(message)
        except:
            break

threading.Thread(target=receive, daemon=True).start()

while True:
    msg = input()
    client.send(f"{name}: {msg}".encode())