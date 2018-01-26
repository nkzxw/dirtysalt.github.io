#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import asyncio
import logging
import time

from autobahn.asyncio.websocket import WebSocketServerFactory, WebSocketServerProtocol
from redis_queue import RedisQueue

# # 这个地方似乎有bug, 如果使用uvloop的话，整个代码会hang住
# import uvloop
#
# asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

global_conns = dict()
global_lock = asyncio.Lock()
command_queue = RedisQueue('command')
logger = logging.getLogger()
DEFAULT_LOGGING_FORMAT = '[%(asctime)s][%(levelname)s]%(filename)s@%(lineno)d: %(msg)s'
logging.basicConfig(level=logging.WARN, format=DEFAULT_LOGGING_FORMAT)


# 决定是否从redis queue里面收取消息然后广播到所有连接上.
def read_command():
    while True:
        item = command_queue.get(timeout=30)
        if item is None:
            continue
        logger.warning('got item {}. write to {} clients'.format(item, len(global_conns)))
        ts = int(time.time())
        msg = str(ts).encode('utf8')
        conns = list(global_conns.values())
        for conn in conns:
            conn.sendMessage(msg)


def write_command():
    idx = 0
    while True:
        command_queue.put('command #%d' % idx)
        idx += 1
        time.sleep(5)


def print_stats():
    while True:
        logger.warning('total connections = {}'.format(len(global_conns)))
        time.sleep(5)


class MyServerProtocol(WebSocketServerProtocol):
    async def onMessage(self, payload, isBinary):
        logger.info('onMessage. {}, {}'.format(payload, isBinary))
        self.sendMessage(b'pong')
        # self.sendMessage(payload, isBinary)

    async def onConnect(self, request):
        self.peer = request.peer
        global global_conns
        with await global_lock:
            global_conns[self.peer] = self
        logger.info('onConnect {}'.format(request))
        pass

    async def onClose(self, wasClean, code, reason):
        global global_conns
        with await global_lock:
            if self.peer in global_conns:
                del global_conns[self.peer]
        logger.info('onClose {}, {}, {}'.format(wasClean, code, reason))
        pass

    async def onOpen(self):
        logger.info('onOpen ...')
        pass


if __name__ == '__main__':
    factory = WebSocketServerFactory()
    factory.protocol = MyServerProtocol
    loop = asyncio.get_event_loop()
    coro = loop.create_server(factory, '127.0.0.1', 8765)
    server = loop.run_until_complete(coro)
    loop.run_in_executor(None, read_command)
    loop.run_in_executor(None, write_command)
    loop.run_in_executor(None, print_stats)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.close()
        loop.close()
