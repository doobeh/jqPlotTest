from flask import Flask, render_template, jsonify
from datetime import datetime, timedelta
import time
from random import randint

app = Flask(__name__)

def js_timestamp(dt):
    """ Return a javascript timestamp from a datetime object.

        Javascript times are milliseconds since the epoch,
        whereas python uses just seconds, so lets return the
        times in the javascript format, so it's unambiguous to
        jqPlot.

    """
    return time.mktime(dt.timetuple()) * 1000


@app.route('/_get_data')
def get_date():
    """ Generate a JSON array of 30 random dates and times """

    data = list()
    start_date = datetime(2012,6,8,12,00)

    for i in range(30):
        random_value = randint(1,1000)
        random_offset = timedelta(minutes=randint(1,1000))
        data.append([js_timestamp(start_date+random_offset), random_value])

    return jsonify(output=data)


@app.route('/')
def home():
    """ Simply serve our chart page """
    return render_template('chart.html')


if __name__ == '__main__':
    app.run(debug=True)

