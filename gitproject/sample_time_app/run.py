from flask import Flask
from datetime import datetime, timedelta
app = Flask(__name__)


@app.route('/time')
def hello_world():
    time = datetime.now()-timedelta(hours=4, minutes=0)
    return time.strftime("%H:%M")


app.run(host='0.0.0.0',
        port=8080,
        debug=True)

