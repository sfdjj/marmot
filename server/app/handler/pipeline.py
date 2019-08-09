#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by wenchao.jia on 19-8-9.
# Mail:wenchao.jia@qunar.com
from aiohttp import web

from server.app.handler import routes, json_response


@routes.get('/test')
async def start_demo(request: web.Request):
    data = [{'tag': 'A', 'dependencies': []},
            {'tag': 'B', 'dependencies': ['A', 'C']},
            {'tag': 'C', 'dependencies': ['A']},
            {'tag': 'D', 'dependencies': ['B', 'C']}]
    return json_response('test_success')
