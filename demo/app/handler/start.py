#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by wenchao.jia on 19-8-1.
# Mail:wenchao.jia@qunar.com
from aiohttp import web

from demo.app.handler import json_response, routes


@routes.get('/start_demo')
async def start_demo(request: web.Request):
    data = [{'tag': 'A', 'dependencies': []},
            {'tag': 'B', 'dependencies': ['A', 'C']},
            {'tag': 'C', 'dependencies': ['A']},
            {'tag': 'D', 'dependencies': ['B', 'C']}]
    return json_response('start_success')
