# CO2 Monitor

The goal of this project is to create a network of CO2 sensors for indoor air quality monitoring. See our [project proposal](https://github.com/EricSchrock/co2-monitor/blob/main/submissions/proposal.pdf) and [project report](https://github.com/EricSchrock/co2-monitor/blob/main/submissions/report.pdf) for more detail on our motivation, goals, design, and results.


&nbsp;
## Design

Our system is composed of a variable number of sensor units, which wirelessly report CO2 readings back to a base station. The base station presents these readings via a locally hosted website.

The base station is a Raspberry Pi 4B. We considered a range of [microcontrollers](https://github.com/EricSchrock/co2-monitor/blob/main/docs/microcontroller.md) and [CO2 sensors](https://github.com/EricSchrock/co2-monitor/blob/main/docs/co2-sensor.md) for the sensor unit. We settled on the Raspberry Pi Pico W connected to a Sparkfun ENS160 sensor over I2C.

| System                         | Sensor Unit                    |
|--------------------------------|--------------------------------|
| <img src="images/system.png"/> | <img src="images/sensor.png"/> |

Note: The CO2 sensor shown in the Fritzing diagram above does not match the actual part and is only meant to give a general sense of the design.


&nbsp;
## Bill of Materials (BOM)

### Base Station

| Part                   | Price* | Supplier  | Link                                                                     |
|------------------------|--------|-----------|--------------------------------------------------------------------------|
| Raspberry Pi 4B (8 GB) | $75.00 | PiShop.us | https://www.pishop.us/product/raspberry-pi-4-model-b-8gb/                |
| 15W power supply       |  $8.00 | PiShop.us | https://www.pishop.us/product/raspberry-pi-15w-power-supply-us-white/    |
| Case                   |  $5.00 | PiShop.us | https://www.pishop.us/product/raspberry-pi-4-case-red-white/             |
| **Total**              | $88.00 |           |                                                                          |

*Price does not include shipping or bulk discounts.

### Sensor Unit

| Part                   | Price* | Supplier  | Link                                                                                |
|------------------------|--------|-----------|-------------------------------------------------------------------------------------|
| Raspberry Pi Pico WH   |  $7.00 | PiShop.us | https://www.pishop.us/product/raspberry-pi-pico-wh/                                 |
| 12.5W power supply     |  $8.00 | PiShop.us | https://www.pishop.us/product/raspberry-pi-12-5w-power-supply-us-white/             |
| Sparkfun ENS160        | $19.95 | SparkFun  | https://www.sparkfun.com/products/20844                                             |
| Half sized bread board |  $4.75 | PiShop.us | https://www.pishop.us/product/half-size-400-pin-diy-breadboard-white/               |
| Breadboard wire kit**  |  $2.32 | PiShop.us | https://www.pishop.us/product/breadboard-wiring-kit/                                |
| Headers for ENS160**   |  $0.35 | PiShop.us | https://www.pishop.us/product/break-away-headers-40-pin-male-long-centered-pth-0-1/ |
| **Total**              | $42.37 |           |                                                                                     |

*Price does not include shipping or bulk discounts. \
**One set is enough to furnish at least three sensor units. Price divided by three.

### System

One system with a base station and three sensor units would cost $215.11 (not accounting for shipping). A productionized system could cost much less by buying in bulk and by using a less powerful Raspberry Pi (e.g. less RAM) in the base station. A productionized system would need to add a protective case for the sensor units.


&nbsp;
## Installation

See [src/README.md](https://github.com/EricSchrock/co2-monitor/blob/main/src/README.md) for instructions on setting up the sensor units, server, and web viewer.


&nbsp;
## Tasks

Hardware
  - [x] [First prototype: Just get something working](https://github.com/EricSchrock/co2-monitor/blob/main/docs/first-prototype.md)
    - [x] Diagram initial system architecture
    - [x] Diagram initial sensor unit
    - [x] [Choose which microcontroller to use for the sensor unit](https://github.com/EricSchrock/co2-monitor/blob/main/docs/microcontroller.md)
    - [x] [Choose which CO2 sensor to use](https://github.com/EricSchrock/co2-monitor/blob/main/docs/co2-sensor.md)
    - [x] Create parts list (including tools)
    - [x] Research/test whether to put a capacitor on the power rail between the microcontroller and CO2 sensor (some microcontrollers have built in capacitance on their power outputs)
    - [x] Research/test whether pull up resistors are needed on the I2C SDA and SCL lines between the microcontroller and CO2 sensor (some microcontrollers have built in or configurable pull ups on pins)
  - [x] Second prototype: Consider cost, size, and power usage
    - [x] Choose breadboard size (mini, tiny, half, or half+)
    - [x] Bill of Materials (BOM) including costs, part numbers, and supplier links

Software
  - [x] Sensor readings displayed on sensor unit (via debugger, attached LCD, etc.)
  - [x] Sensor readings displayed on base station (over wifi)
  - [x] Sensor readings displayed on locally hosted website served from the base station
    - [x] Live readings
    - [x] Historical trends
    - [x] Multiple sensors
  - [x] Diagrams (flow charts, activity diagrams, and/or sequence diagram)
    - [x] Sensor unit (sensor.py)
    - [x] Base station (server.py)
    - [x] Whole system

&nbsp;
## Resources

 - <https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html>
 - <https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/0>
 - <https://datasheets.raspberrypi.com/picow/connecting-to-the-internet-with-pico-w.pdf>
 - <https://cdn.sparkfun.com/assets/3/c/7/5/5/SC-001224-DS-7-ENS160-Datasheet.pdf>
