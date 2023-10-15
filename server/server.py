import selectors
import signal
import socket
import logging
import atexit

import config
import data_writer

logging.basicConfig(filename='server.log', datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)s, %(message)s', level=logging.INFO)

selector = selectors.DefaultSelector()

interrupt_read, interrupt_write = socket.socketpair()
selector.register(interrupt_read, selectors.EVENT_READ)
signal.signal(signal.SIGINT, lambda x, y: interrupt_write.send(b'\0'))
signal.signal(signal.SIGTERM, lambda x, y: interrupt_write.send(b'\0'))

server = socket.socket(type=socket.SOCK_STREAM | socket.SOCK_NONBLOCK)
server.bind((config.IP, config.PORT))
selector.register(server, selectors.EVENT_READ)

@atexit.register
def cleanup() -> None:
    for key in list(selector.get_map().values()):
        selector.unregister(key.fileobj)
        key.fileobj.close()
    selector.close()
    logging.info('End server')

def accept() -> None:
    client, (ip, port) = server.accept()
    uid = client.recv(config.BUFFER).decode()
    logging.info(f'Accept client {uid} at {ip}:{port}')
    client.setblocking(False)
    selector.register(client, selectors.EVENT_READ, uid)

def read(client, uid) -> None:
    if data := client.recv(config.BUFFER):
        data_writer.write(uid, data.decode())
    else:
        logging.info(f'Close client {uid}')
        selector.unregister(client)
        client.close()

logging.info(f'Start server at {config.IP}:{config.PORT}')
server.listen(config.SENSORS)
while True:
    for key, _ in selector.select():
        if key.fileobj == interrupt_read:
            raise SystemExit
        elif key.fileobj == server:
            accept()
        else:
            read(key.fileobj, key.data)
