from flask import Flask
import time

app = Flask(__name__)


@app.route('/bobo')
def index_bobo():
    time.sleep(2)
    return 'Hello bobo'


@app.route('/zs')
def index_zs():
    time.sleep(2)
    return 'Hello zs'


@app.route('/ls')
def index_ls():
    time.sleep(2)
    return 'Hello ls'


if __name__ == '__main__':
    app.run(threaded=True)
