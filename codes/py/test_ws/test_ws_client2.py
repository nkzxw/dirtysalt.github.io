#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


import asyncio
import logging
import time

from autobahn.asyncio.websocket import WebSocketClientFactory, WebSocketClientProtocol
from tdigest import TDigest

global_index = 0
logger = logging.getLogger()
DEFAULT_LOGGING_FORMAT = '[%(asctime)s][%(levelname)s]%(filename)s@%(lineno)d: %(msg)s'
logging.basicConfig(level=logging.WARN, format=DEFAULT_LOGGING_FORMAT)


class Digest:
    def __init__(self):
        self.digest = TDigest()
        self.digest.update(0)

    def clear(self):
        self.digest = TDigest()
        self.digest.update(0)

    def add(self, v):
        self.digest.update(v)

    def percentile(self, v):
        return self.digest.percentile(v)


digest = Digest()


# 打印ping-pong的延迟情况
def print_digest():
    global digest
    while True:
        logger.warning('DIGEST p50 = {}, p75 = {}, p90 = {}, p99 = {}'.format(digest.percentile(50),
                                                                              digest.percentile(75),
                                                                              digest.percentile(90),
                                                                              digest.percentile(99)))
        digest.clear()
        time.sleep(5)


class MyClientProtocol(WebSocketClientProtocol):
    def onConnect(self, response):
        logger.info('on Connect ...')
        global global_index
        self.index = global_index
        global_index += 1

    def onOpen(self):
        logger.info('on Open... ')
        self.sendMessage(b'ping')
        self.ping = time.time()
        pass

    def onMessage(self, payload, isBinary):
        if payload != b'pong':
            return

        now = time.time()
        latency = now - self.ping
        global digest
        digest.add(latency * 1000)
        logger.info('inst#{} recv {}. latency = {}'.format(self.index, payload, latency))
        # await asyncio.sleep(5)
        self.sendMessage(b'ping')
        self.ping = time.time()


if __name__ == '__main__':
    factory = WebSocketClientFactory()
    factory.protocol = MyClientProtocol

    loop = asyncio.get_event_loop()
    inst_num = 10000
    insts = []
    for i in range(inst_num):
        coro = loop.create_connection(factory, '127.0.0.1', 8765)
        insts.append(coro)

    loop.run_until_complete(asyncio.gather(*insts))
    loop.run_in_executor(None, print_digest)
    loop.run_forever()
    loop.close()
