from pathlib import Path
from flask import Flask, render_template, request
import datetime

from viewer.image import image
from viewer.config import sensors

app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
@app.route('/index', methods=('GET', 'POST'))
def index():
    return render_template(
        'index.html',
        data=image(request.form['date'] if request.method == 'POST' else '',
                   request.form['sensor'] if request.method == 'POST' else ''),
        sensors=sensors
        )
