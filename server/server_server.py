#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by wenchao.jia on 19-8-1.
# Mail:wenchao.jia@qunar.com
import os

import aiomonitor
import asyncio

import uvloop
from aiohttp import web
from tornado.httpclient import AsyncHTTPClient
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from server.app.handler import routes

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
AsyncHTTPClient.configure(SimpleAsyncHTTPClient, max_clients=10000, defaults=dict(request_timeout=400))


def import_sub_modules(dir_name):
    """
    导入该目录下的所有模块
    :param dir_name:
    :return:
    """
    root_path = os.path.dirname(__file__)
    for file in os.listdir(os.path.join(root_path, dir_name)):
        if file.startswith('_') or file.endswith('.pyc'):
            continue
        file = os.path.join(dir_name, file)
        if file.endswith('.py'):
            __import__(file[:-3].replace('/', '.'))
        else:
            __import__(file.replace('/', '.'))

        if os.path.isdir(os.path.join(root_path, file)):
            import_sub_modules(file)


if __name__ == '__main__':
    path = os.path.dirname(__file__)
    import_sub_modules('app')
    app = web.Application()
    app.add_routes(routes)
    print(routes)
    with aiomonitor.start_monitor(asyncio.get_event_loop()):
        web.run_app(app, port=9001)
