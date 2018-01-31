#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import logging
import os

from flask import Flask, request
from flask_socketio import Namespace, SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, message_queue='redis://localhost/0', channel='flask-socketio')
logger = logging.getLogger('server')
DEFAULT_LOGGING_FORMAT = '[%(asctime)s][%(levelname)s]%(filename)s@%(lineno)d: %(msg)s'
logging.basicConfig(level=logging.WARN, format=DEFAULT_LOGGING_FORMAT)


@app.route('/', methods=['GET'])
@app.route('/room/<int:room>/', methods=['GET'])
def index(room=0):
    logger.warning(request.environ['REMOTE_ADDR'], request.environ['REMOTE_PORT'], room)
    # return render_template('index.html')
    return 'OK'


class FanoutNamespace(Namespace):
    path = '/fanout.%s' % (os.getpid())

    def on_connect(self):
        logger.warning('path = {}, on connect sid = {}, ({}:{})'.format(
            self.path, request.sid, request.environ['REMOTE_ADDR'],
            request.environ['REMOTE_PORT']))

    def on_disconnect(self):
        pass

    def on_message(self, message):
        pass

    def on_my_event(self, message):
        pass


socketio.on_namespace(FanoutNamespace('/fanout'))

if __name__ == '__main__':
    import sys

    port = 8080
    if len(sys.argv) >= 2:
        port = int(sys.argv[1])
    socketio.run(app, debug=True, port=port)
