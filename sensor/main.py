from machine import Pin, unique_id
from network import STA_IF, STAT_CONNECTING, WLAN
from socket import socket
from time import sleep, sleep_ms

from config import SSID, PWD, IP, PORT
from ens160 import ENS160

led = Pin("LED", Pin.OUT)

wlan = WLAN(STA_IF)
wlan.active(True)
wlan.connect(SSID, PWD)
while wlan.status() == STAT_CONNECTING:
    led.toggle()
    sleep_ms(250)
if wlan.isconnected():
    led.on()

sensor = ENS160()         # CO2 Sensor attached via I2C
sensor.opmode(0x02)       # Enable sensor readings
uid = unique_id().hex()   # Unique device ID
while True:
    try:
        client = socket()
        client.connect((IP, PORT))
        client.sendall(uid.encode())
        while True:
            led.on()
            client.sendall(str(sensor.eco2()).encode())
            led.off()
            sleep(30)
    except OSError:
        client.close()
        led.on()
        sleep(60)
