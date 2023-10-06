
## Microcontroller Comparison

| Microcontroller | Price* | Shipping  | Headers** | 3V3 | 5V  | I2C    | BT  | BLE | Fritzing  | Link |
|-----------------|--------|-----------|-----------|-----|-----|--------|-----|-----|-----------|------|
| Micro           | $24.90 |    3 days |       Yes | Yes | Yes | Yes    |  No |  No |   Yes**** | https://store-usa.arduino.cc/products/arduino-micro |
| Nano            | $24.90 |    3 days |       Yes | Yes | Yes | Yes    |  No |  No |   Yes     | https://store-usa.arduino.cc/products/arduino-nano |
| Nano Every      | $14.70 |    3 days |       Yes | Yes | Yes | Yes    |  No |  No |   Yes**** | https://store-usa.arduino.cc/products/arduino-nano-every-with-headers |
| Nano 33 BLE     | $29.30 |    3 days |       Yes | Yes | Yes | Yes*** | Yes | Yes |   Yes**** | https://store-usa.arduino.cc/products/arduino-nano-33-ble-with-headers |
| Nano 33 IoT     | $27.00 |    3 days |       Yes | Yes | Yes | Yes*** | Yes | Yes |   Yes**** | https://store-usa.arduino.cc/products/arduino-nano-33-iot-with-headers |
| Nano ESP32      | $21.00 |    3 days |       Yes | Yes | Yes | Yes    | Yes |  No |    No     | https://store-usa.arduino.cc/products/nano-esp32-with-headers |
| RPi Pico WH     |  $7.00 | 1-5+ days |       Yes | Yes | Yes | Yes    | Yes | Yes |   Yes     | https://www.sparkfun.com/products/20174 |

RPi Pico WH just went out of stock on Sparkfun, it is also available at
<https://www.pishop.us/product/raspberry-pi-pico-wh/>

*Does not include shipping \
**Breadboard compatible headers \
***Built in pull up resistors \
****Custom Fritzing part available to download


&nbsp;
## Microcontroller Choice

We started our search with the Arduino Micro and Nano because we want to keep our sensor units small and cheap. We plan to build our prototypes on small breadboards, so having pre-soldered headers that fit breadboard rails will keep things simple. We anticipate communicating with our CO2 sensor over I2C but we don't know yet whether the sensor we choose will require 3V3 or 5V power. Power usage is also a consideration for our project so we'd like to use BLE rather than vanilla Bluetooth if possible The Nano 33 IoT is the cheapest Arduino that checks all the boxes.

The key features for the Sensor Processing unit are energy requirements, wireless
communication ability, and cost. The goal is to have a scalable network of
deployed sensors throughout a building, so minimizing the cost and energy
requirements of each unit is desirable. However, networking ability is a
necessity.

The Raspberry Pi Pico WH has the following pros
    - Low Cost: Only $7.00 per unit
  - Versatile Power input: 5V via micro USB or 1.8V - 5.5 V from any power
    source directly to VSYS (battery, etc.) with automatic conversion to 3V3
    via onboard buck-boost SMPS.
  - Full Wireless Capabilities: 2.4GHz wireless interface (Infineon CYW4343)
    - Single band (2.4 GHz) Wifi 4 (802.11n)
    - WPA3
    - softAP (up to 4 clients)
    - Bluetooth 5.2:
      - Support for Bluetooth LE Central and Peripheral roles
      - Support for Bluetooth Classic
  - Available with soldered 0.1 inch headers
  - 30 mulit-function GPIO with 1.8 - 3.3V I/O
  - 2 UART, 2 SPI, 16 PWM, 4 ADC channels
  - 1 timer with 4 alarms, 1 real time clock
  - 2 Programmable I/O (PIO) blocks, 8 state machines total
  - Fritzing Part
<https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html>

