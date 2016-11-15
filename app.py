from flask import Flask, request
import logging
import sqlite3

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/example/<label>', methods=['GET'])
def example_route(label=None):
    """
    An example route that can be reached as /example/<label>?param=[param]
    """
    param = request.args.get('param')
    logging.info('Received param: {}'.format(param))
    return 'Label: {}, Param:{}'.format(label, param)


if __name__ == '__main__':
    app.run()

