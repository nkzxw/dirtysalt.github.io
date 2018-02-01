#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import argparse
import time

from gevent import monkey
from gevent.pool import Pool

monkey.patch_all()

import logging
from socketIO_client import BaseNamespace, SocketIO

logger = logging.getLogger('client')
DEFAULT_LOGGING_FORMAT = '[%(asctime)s][%(levelname)s]%(filename)s@%(lineno)d: %(msg)s'
logging.basicConfig(level=logging.WARN, format=DEFAULT_LOGGING_FORMAT)
current_conn_number = 0


class FanoutNamespace(BaseNamespace):
    def on_connect(self):
        global current_conn_number
        logger.info('on connect')
        current_conn_number += 1

    def on_disconnect(self):
        global current_conn_number
        logger.info('on disconnect')
        current_conn_number -= 1

    def on_message(self, data):
        logger.info('on message. msg = {}'.format(data))

    def on_my_event(self, data):
        logger.info('on my event. msg = {}'.format(data))


parser = argparse.ArgumentParser()
parser.add_argument('--batch-size', action='store', default=10, type=int)
parser.add_argument('--batch-round', action='store', default=10, type=int)
parser.add_argument('--port', action='store', default=8080, type=int)
parser.add_argument('--namespace', action='store', default='/fanout', type=str)
parser.add_argument('--host', action='store', default='127.0.0.1', type=str)
parser.add_argument('--bind', action='store', default='127.0.0.1', type=str)
args = parser.parse_args()

batch_size = args.batch_size
batch_round = args.batch_round
total_conn_number = batch_round * batch_size
pool = Pool()
socks = []
port = args.port
host = args.host

for rnd in range(batch_round):
    logger.warning('round #{} start'.format(rnd))
    exp_conn_number = (rnd + 1) * batch_size
    for i in range(batch_size):
        socketIO = SocketIO(host=host, port=port)
        notificiation_namespace: BaseNamespace = socketIO.define(FanoutNamespace, args.namespace)
        socks.append(socketIO)
        pool.spawn(socketIO.wait)
    while current_conn_number != exp_conn_number:
        logger.warning('current_conn = {}, exp_conn = {}'.format(current_conn_number, exp_conn_number))
        time.sleep(5)
    logger.warning('round #{} ok. current_conn = {}'.format(rnd, current_conn_number))

pool.join()
