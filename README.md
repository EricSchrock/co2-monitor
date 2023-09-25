# CO2 Monitor

## Summary

The goal of this project is to create a network of CO2 sensors for indoor air quality monitoring. See our [project proposal](https://github.com/EricSchrock/co2-monitor/blob/main/submissions/proposal.pdf) for more detail on our motivation and goals.


&nbsp;
### System Architecture

![Alt Text](docs/system-architecture.png?raw=true)


&nbsp;
### Sensor Unit

![Alt Text](docs/CO2-sensor-unit.png?raw=true)


&nbsp;
## Tasks

 - Hardware
   - [ ] First prototype: Just get something working
     - [x] Diagram initial system architecture
     - [x] Diagram initial sensor unit
     - [ ] Choose which Arduino to use for the sensor unit
     - [ ] Choose which CO2 sensor to use
     - [ ] Create parts list (including tools)
     - [ ] Research/test whether to put a capacitor on the power rail between the Arduino and CO2 sensor
     - [ ] Research/test whether pull up resistors are needed on the I2C SDA and SCL lines between the Arduino and CO2 sensor
   - [ ] Second prototype: Consider cost, size, and power usage
     - [ ] Choose breadboard size (mini, tiny, half, or half+)
     - [ ] Bill of Materials (BOM) including costs, part numbers, and supplier links
     - [ ] Create a [custom Fritzing part](https://fritzing.org/learning/tutorials/creating-custom-parts) for the CO2 sensor
 - Software
   - [ ] Sensor readings displayed on sensor unit (debugger, attached LCD, etc.)
   - [ ] Sensor readings displayed on base unit (over Bluetooth or BLE)
   - [ ] Sensor readings displayed on LAN website hosted on base unit
     - [ ] Live readings
     - [ ] Historical trends
     - [ ] Multiple sensors


&nbsp;
## Resources

1. [Arduino I2C guide](https://docs.arduino.cc/learn/communication/wire)
2. [Arduino BLE guide](https://docs.arduino.cc/tutorials/nano-33-ble-sense/ble-device-to-device)
