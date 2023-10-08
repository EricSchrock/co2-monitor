# Save this file to the Pico as "main.py" to have it run on startup

from machine import Pin
from time import sleep

led = Pin("LED", Pin.OUT)

while True:
    led.toggle()
    sleep(1)
