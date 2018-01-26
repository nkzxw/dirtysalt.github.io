#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import asyncio
import logging

from autobahn.asyncio.websocket import WebSocketClientFactory, WebSocketClientProtocol

global_index = 0
logger = logging.getLogger()
DEFAULT_LOGGING_FORMAT = '[%(asctime)s][%(levelname)s]%(filename)s@%(lineno)d: %(msg)s'
logging.basicConfig(level=logging.WARN, format=DEFAULT_LOGGING_FORMAT)


# client连接上之后就只接收消息
class MyClientProtocol(WebSocketClientProtocol):
    def __init__(self):
        global global_index
        self.index = global_index
        global_index += 1

    def onOpen(self):
        # logger.info('on Open... ')
        pass

    def onMessage(self, payload, isBinary):
        logger.info('inst#{} recv {}'.format(self.index, payload))


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
    loop.run_forever()
    loop.close()
