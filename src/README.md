# Sensor Setup

Modify `sensor/config.py` to set `SSID` and `PWD` to match the wifi network
your server is connected to. Set `IP` to the IP of the server and choose a
`PORT` number.

Save `sensor/config.py`, `sensor/ens160.py`, and `sensor/main.py` to the Raspberry
Pi Pico WH on each sensor. One way to do this is with the [Thonny](https://thonny.org/)
editor. The Pico will run `main.py` on power on.

Plug all your sensors into power. The LED on the Pico will blink until a wifi
connection is complete and then stay on until it connects to the server. Then
it will blink each time data is transmitted.

# Server Setup

## Configure Server

Modify the file `server/config.py` to set the Server IP address and Port.
These values must match the configuration hardcoded in the sensors.

Additionally, set the `SENSORS` value to the number of sensors that will be
connected to the system.

##  Run Server

```sh
python3 server/server.py
```

The server log and the CO2 data received will be stored in `~/.co2_data`. Add
the following line to `/etc/rc.local` to start the server on power on.

```sh
python3 /home/<user>/co2-monitor/src/server/server.py &
```

This assumes you have this repo checked out in your home directory.

# Web Viewer Setup

## Create and activate the venv

```sh
python3 -m venv .venv
source .venv/bin/activate
```

## Install requirements

```sh
python3 -m pip install -r requirements.txt
```

## Configure Web Viewer

Modify the dictionary in in `viewer/config.py` to map the sensor
unique IDs to more useful identifiers to be displayed in the webpage.

The unique IDs for the sensors connected to your system can be found
in the server log at `$HOME/.co2_data/server.log`.

## Run Web Viewer for development

To start the web viewer in development mode, run

```sh
flask -A viewer run --debug
```

This will start the http server on you local host at
`http://127.7.7.1:5000`.

## Run Web Viewer for deployment

To start the web viewer in deploy mode, start the http server using
`waitress` with

```sh
waitress-serve viewer:app
```

This will start the http server on `http://0.0.0.0:8080`, which will
serve the webpage from all IP addresses on your pi on port 8080. You can
navigate to `http://<rpi hostname>.local:8080` or `http://<rpi IP>:8080`
to view the web page.

## Using the Web Viewer

The web viewer will default to showing you a chart with all sensor values for
the current day. Using the available form fields, you can optionally specify to
view specific sensors or any other date. If no sensor data is available for the
selected date and sensor, no image will be shown.
