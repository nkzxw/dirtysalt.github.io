#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import logging
import queue
import threading
import time

from gevent import monkey
from gevent.pool import Pool

monkey.patch_all()

import rabbitpy

logger = logging.getLogger(__name__)


class Connection:
    def __init__(self, **kwargs):
        url = kwargs.get('url', '')
        self._conn = rabbitpy.Connection(url)
        self._chan = self._conn.channel()
        self._pool = None
        self._ident = None
        self._kwargs = kwargs
        self._closed = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if isinstance(exc_val, rabbitpy.exceptions.RabbitpyException):
            logger.debug('Got exception. type = {}, value = {}, tb = {}'.format(exc_type, exc_val, exc_tb))
            self.close()
        self._pool.release(self)

    def __str__(self):
        return 'Connection(ident = {}, kwargs = {})'.format(self._ident, self._kwargs)

    def close(self):
        if not self._closed:
            self._closed = True
            self._chan.close()
            if not self._conn.closed:
                self._conn.close()

    def set_pool(self, pool):
        self._pool = pool

    def set_ident(self, ident):
        self._ident = ident

    @property
    def channel(self):
        return self._chan

    @property
    def closed(self):
        return self._closed


class ConnectionPool:
    def __init__(self, conn_class=None, **conn_kwargs):
        self._conn_class = conn_class or Connection
        self._conn_kwargs = conn_kwargs
        self._avaiable = queue.Queue()
        self._lock = threading.Lock()
        self._in_use = set()
        self._conn_number = 0

    def acquire(self):
        with self._lock:
            try:
                conn = self._avaiable.get_nowait()
                return conn
            except queue.Empty:
                conn_number = self._conn_number
                self._conn_number += 1
                pass
        conn = self._conn_class(**self._conn_kwargs)
        conn.set_pool(self)
        conn.set_ident('%d' % conn_number)
        with self._lock:
            self._in_use.add(conn)
        return conn

    def release(self, conn):
        with self._lock:
            if conn.closed:
                self._in_use.remove(conn)
            else:
                self._avaiable.put(conn)

    def close(self):
        logger.debug('# of in_use = {}'.format(len(self._in_use)))
        for conn in self._in_use:
            conn.close()

    @property
    def in_use_size(self):
        return len(self._in_use)


class MessageQueue(ConnectionPool):
    def __init__(self, name, exchange=None, conn_class=None, **conn_kwargs):
        self._name = name
        self._exchange = exchange
        super(MessageQueue, self).__init__(conn_class=conn_class, conn_kwargs=conn_kwargs)

    def declare(self, durable=False):
        with self.acquire() as conn:
            logger.debug('declare conn = {}'.format(conn))
            q = rabbitpy.Queue(conn.channel, self._name)
            q.durable = durable
            q.declare()

    def consume(self, callback):
        with self.acquire() as conn:
            logger.debug('consume conn = {}'.format(conn))
            queue = rabbitpy.Queue(conn.channel, self._name)
            for message in queue.consume(prefetch=1):
                callback(message)
                message.ack()


def main():
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logging.Formatter(logging.BASIC_FORMAT))
    logger.addHandler(handler)
    url = 'amqp://localhost:5672/%2F'
    mq = MessageQueue(name='hello2', url=url)

    def run():
        # mq.declare(durable=True)

        def cb(message):
            logger.info(message.body.decode('utf8'))
            time.sleep(5)

        while True:
            try:
                mq.consume(cb)
            except rabbitpy.exceptions.RabbitpyException as e:
                logger.warning('rabbitpy excepiton')
            except Exception as e:
                logger.warning('general exception')

    def watch():
        while True:
            logger.info('in use size = {}'.format(mq.in_use_size))
            time.sleep(2)

    pool = Pool()
    for i in range(4):
        pool.spawn(run)
    pool.spawn(watch)
    pool.join()
    mq.close()


if __name__ == '__main__':
    main()
