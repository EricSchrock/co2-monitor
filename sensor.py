# Save this file to the Pico as "main.py" to have it run on startup

from machine import I2C, Pin
from time import sleep

led = Pin("LED", Pin.OUT)
i2c = I2C(0, scl=Pin("GP17"), sda=Pin("GP16"))

while True:
    led.toggle()
    value = 0x2
    i2c.writeto_mem(0x53, 0x10, value.to_bytes(1, 'little'))
    mode = int.from_bytes(i2c.readfrom_mem(0x53, 0x10, 1), 'little')
    co2 = int.from_bytes(i2c.readfrom_mem(0x53, 0x24, 2), 'little')
    print(f"co2: {co2}")
    sleep(0.1)
