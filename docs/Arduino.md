
## Arduino Comparison

| Arduino     | Price  | Shipping | Headers* | 3V3 | 5V  | I2C   | BT  | BLE | Fritzing | Link |
|-------------|--------|----------|----------|-----|-----|-------|-----|-----|----------|------|
| Micro       | $24.90 |   3 days |      Yes | Yes | Yes | Yes   |  No |  No |   Yes*** | https://store-usa.arduino.cc/products/arduino-micro |
| Nano        | $24.90 |   3 days |      Yes | Yes | Yes | Yes   |  No |  No |   Yes    | https://store-usa.arduino.cc/products/arduino-nano |
| Nano Every  | $14.70 |   3 days |      Yes | Yes | Yes | Yes   |  No |  No |   Yes*** | https://store-usa.arduino.cc/products/arduino-nano-every-with-headers |
| Nano 33 BLE | $29.30 |   3 days |      Yes | Yes | Yes | Yes** | Yes | Yes |   Yes*** | https://store-usa.arduino.cc/products/arduino-nano-33-ble-with-headers |
| Nano 33 IoT | $27.00 |   3 days |      Yes | Yes | Yes | Yes** | Yes | Yes |   Yes*** | https://store-usa.arduino.cc/products/arduino-nano-33-iot-with-headers |
| Nano ESP32  | $21.00 |   3 days |      Yes | Yes | Yes | Yes   | Yes |  No |    No    | https://store-usa.arduino.cc/products/nano-esp32-with-headers |

*Breadboard compatible headers \
**Built in pull up resistors \
***Custom Fritzing part available to download


&nbsp;
## Arduino Choice

We started our search with the Arduino Micro and Nano because we want to keep our sensor units small and cheap. We plan to build our prototypes on small breadboards, so having pre-soldered headers that fit breadboard rails will keep things simple. We anticipate communicating with our CO2 sensor over I2C but we don't know yet whether the sensor we choose will require 3V3 or 5V power. Power usage is also a consideration for our project so we'd like to use BLE rather than vanilla Bluetooth if possible The Nano 33 IoT is the cheapest Arduino that checks all the boxes.
