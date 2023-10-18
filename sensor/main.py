from machine import ADC, Pin, unique_id
import network
import socket
import time

from config import SSID, PWD, IP, PORT
from ens160 import ENS160

LED = Pin("LED", Pin.OUT)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PWD)
while wlan.status() == network.STAT_CONNECTING:
    LED.toggle()
    time.sleep_ms(250)
if wlan.isconnected():
    LED.on()

sensor = ENS160()         # CO2 Sensor attached via I2C
sensor.opmode(0x02)       # Enable sensor readings
uid = unique_id().hex()   # Unique device ID
while True:
    try:
        client = socket.socket()
        client.connect((IP, PORT))
        client.sendall(uid.encode())
        while True:
            LED.on()
            client.sendall(str(sensor.eco2()).encode())
            LED.off()
            time.sleep(30)
    except OSError:
        client.close()
        LED.on()
        time.sleep(60)
