#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import argparse
import time

import tdigest
from gevent import monkey
from gevent.pool import Pool

monkey.patch_all()

import logging
from socketIO_client import BaseNamespace, SocketIO
from socket import socket as Socket

logger = logging.getLogger('client')
DEFAULT_LOGGING_FORMAT = '[%(asctime)s][%(levelname)s]%(filename)s@%(lineno)d: %(msg)s'
logging.basicConfig(level=logging.WARN, format=DEFAULT_LOGGING_FORMAT)
current_conn_number = 0
rcv_msg_number = 0
digest = tdigest.TDigest()


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
        # logger.info('on my event. msg = {}'.format(data))
        ts = int(data)
        now = int(time.time() * 1000)
        delay = (now - ts)
        digest.update(delay)
        global rcv_msg_number
        rcv_msg_number += 1


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

_socket_connect = Socket.connect


def my_socket_connect(self: Socket, address):
    # logger.warning('socket {} bind to {}'.format(self, args.bind))
    self.bind((args.bind, 0))
    return _socket_connect(self, address)


Socket.connect = my_socket_connect

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

while rcv_msg_number != total_conn_number:
    logger.warning('rcv_msg = {}, total_conn = {}'.format(rcv_msg_number, total_conn_number))
    time.sleep(5)
for s in socks:
    s.disconnect()
logger.warning(
    'digest. p50 = {}, p90 = {}, p99 = {}'.format(
        digest.percentile(50), digest.percentile(90), digest.percentile(99)))
pool.join()
