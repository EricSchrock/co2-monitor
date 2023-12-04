from pathlib import Path
import base64
import io
import datetime

import numpy as np
from matplotlib.figure import Figure
from matplotlib.ticker import MultipleLocator
from matplotlib.dates import AutoDateLocator, ConciseDateFormatter

from viewer.config import sensors

def load(file: Path):
    ppm = np.loadtxt(file, delimiter=',', usecols=1, dtype=np.uint)
    time = np.loadtxt(file, delimiter=',', usecols=0, dtype=str)
    time = np.char.add(f'{file.parent.stem}T', time).astype(np.datetime64)
    return time, ppm

def image(date: str, sensor: str):
    # Accepts empty strings, in which case use today and all sensor files
    if not date:
        date = datetime.date.today().isoformat()
    date_dir = Path.home()/'.co2_data'/date
    if not date_dir.is_dir():
        return b''  # TODO have a message indicating no data exists
    if sensor and not (date_dir/f'{sensor}.csv').is_file():
        return b''

    fig = Figure()
    ax = fig.add_subplot()
    ax.grid(which='major', axis='y', alpha=0.35)
    ax.set_ylabel('CO2 Levels [ppm]')
    ax.yaxis.set_major_locator(MultipleLocator(400))
    ax.yaxis.set_minor_locator(MultipleLocator(100))
    ax.set_xlabel('Time')
    date_locator = AutoDateLocator()
    ax.xaxis.set_major_locator(date_locator)
    ax.xaxis.set_major_formatter(ConciseDateFormatter(date_locator))
    ax.set_ylim((400, 2000))

    if sensor:
        ax.set_title(sensors.get(sensor))
        time, ppm = load(date_dir/f'{sensor}.csv')
        ax.scatter(time, ppm, s=0.5)
    else:
        for sensor in sensors:
            time, ppm = load(date_dir/f'{sensor}.csv')
            ax.scatter(time, ppm, s=0.5, label=sensors.get(sensor))
        ax.legend()

    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    return base64.b64encode(buf.getbuffer()).decode('ascii')
