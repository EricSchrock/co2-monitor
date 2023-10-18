import socket
import time
import random
from config import IP, PORT, SENSORS # Set IP = 'localhost' to test the clients and host on the same machine

clients = []
for i in range(SENSORS):
    clients.append(socket.create_connection((IP, PORT)))
    clients[-1].sendall(f'{i:16d}'.encode())
try:
    while True:
        for i in range(SENSORS):
            value = str(round(random.random()*1000, 2))
            print(f'sensor {i} sending {value}')
            clients[i].sendall(value.encode())
            time.sleep(1)
except:
    for client in clients:
        client.close()
