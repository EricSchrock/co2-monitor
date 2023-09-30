
## CO2 Sensor Comparison

| Source   | Price* | Shipping | Vin       | IO  | Link |
|----------|--------|----------|-----------|-----|------|
| Amazon   | $13.99 |   1 day  | 3V3 or 5V | I2C | https://www.amazon.com/EC-Buying-Formaldehyde-Monitoring-Multi-Pixel/dp/B0B389LQCQ/ref=sr_1_3?crid=156HZH08J4OPY&keywords=arduino+CO2+sensor&qid=1695575083&sprefix=arduino+co2+sensor%2Caps%2C97&sr=8-3 |
| Amazon   | $21.99 |   2 days |      2-5V | I2C | https://www.amazon.com/Measurement-Quality-Dioxide-Detector-Replace/dp/B09SH53B58/ref=sr_1_1?crid=156HZH08J4OPY&keywords=arduino+CO2+sensor&qid=1695575083&sprefix=arduino+co2+sensor%2Caps%2C97&sr=8-1 |
| Amazon   | $13.36 |   weeks  |         ? | I2C | https://www.amazon.com/dp/B0CJR2SG1J/ref=sr_1_7?crid=10F62R51MYE61&keywords=arduino+CO2+sensor+module&qid=1695675705&sprefix=arduino+co2+sensor+module%2Caps%2C116&sr=8-7 |
| Arduino  | $48.90 |   3 days |        ?** | ?** | https://store-usa.arduino.cc/collections/sensors/products/gravity-analog-co2-gas-sensor-mg-811-sensor |
| SparkFun | $19.95 |  5+ days |        3V3 | I2C | https://www.sparkfun.com/products/20844 |
| SparkFun | $29.95 |  5+ days |        3V3 | I2C | https://www.sparkfun.com/products/22858 |
| Adafruit | $44.95 |          |     3.3-5V | I2C | https://www.adafruit.com/product/5187 |

*Does not include shipping \
**May require additional Arduino shield (compatible with Nano?)


&nbsp;
## CO2 Sensor Choice

Which CO2 sensor to use is a difficult choice. Well known suppliers like Arduino, SparkFun, and Adafruit likely have better support and documentation, but they are also more expensive and have costlier and slower shipping. Off brand Amazon options are cheap and ship quickly but who knows how well they work or how they they are documented.

There are a few options for CO2 sensing:
- Using "true" CO2 sensors
  - Pros: higher accuracy, direct CO2 measurement
  - Cons: more expensive
- Using "equivalent" CO2 sensors
  - Pros: Cheaper
  - Cons: Don't actually measure CO2, may require calibration, less accurate
- Using combination of "true" and "equivalent" CO2 sensors
  - Pros: single "true" sensor can be used to calibrate "equivalent" sensors
  - Cons: Even a single "true" unit is pretty expensive, extra work to
    integrate two different types of sensors

For this project, the goal is not perfect sensing but instead relative sensing
over time to get a sense of overall air circulation. Because of this, the cost
savings of cheaper CO2 equivalent sensors better meet the needs of the project
than the more accurate true CO2 sensors. Additionally, with multiple sensors
calibration can be done over all the sensors in the same environment, allowing
slight variations per sensor to be balanced out over the whole sensor group.
This means the highest priorities are cost, compatibility, and ease of use.

In the equivalent CO2 sensor space, the
[ENS160](https://www.sciosense.com/wp-content/uploads/documents/SC-001224-DS-9-ENS160-Datasheet.pdf)
appears to offer the perfect balance of quality, cost, and ease of use. For our
system, we are not able to directly solder sensors to our microcontroller PCB,
so we need to buy the sensor on a prefabricated chip with easy pin access. Both
[Sparkfun](https://www.sparkfun.com/products/20844) and
[Adafruit](https://www.adafruit.com/product/5606) offer the ENS160 presoldered
in a convenient package, though at more than double the price of the sensor
itself. Pairing the ENS160 with a temperature and humidity sensor can increase
the accuracy of the results, but for the same price it would be possible to
move into the true CO2 sensing space. We could also have a "central" Humidity
and temperature sensor, say at the hub, that transmits to all of the networked
CO2 sensors using the assumption that the indoor climate is approximately the
same for all sensors.

To move into true CO2 sensors, the
[SCD4x](https://sensirion.com/media/documents/48C4B7FB/64C134E7/Sensirion_SCD4x_Datasheet.pdf)
range of sensors provide varying degrees of accuracy, detection range, and
cost. For this project, the SCD40 has the best balance of low price and
accuracy at the desired detection range (400 - 2000 ppm). The SCD41 sits at a
slightly higher price point and has a larger detection range, but that is not
necessary for the levels of CO2 we are targeting. The only real benefit to the
SCD41 for our project would be the lower power modes that it supports. Again,
both [Sparkfun](https://www.sparkfun.com/products/22395) and
[Adafruit](https://www.adafruit.com/product/5187) provide the SCD40 on a
presoldered package, but the Adafruit product is significantly cheaper.
Adafruit also offers the [SCD41](https://www.adafruit.com/product/5190) for
only $5 more than the SCD40.

I propose we start with the
[Sparkfun ENS160](https://www.sparkfun.com/products/20844), which could either
be directly attached to the RPi via connector pins or could be attached using
the Sparkfun Qwiic system and the
[Qwiick shim](https://www.sparkfun.com/products/15794). If we feel we need more
accuracy, we could either move into the centralized Humidity/Temperature space
or order an SCD4x for calibrating the sensors.
