#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by wenchao.jia on 19-8-1.
# Mail:wenchao.jia@qunar.com
from json import dumps

from aiohttp import web
from aiohttp.web_response import Response

routes = web.RouteTableDef()


def json_response(data, status=0, message='', http_status=200, content_type='application/json'):
    if isinstance(data, Exception):
        message = '系统异常'
        status = -1
        data = ''
    text = dumps({'message': message, 'status': status, 'data': data})
    return Response(text=text, status=http_status, content_type=content_type)
