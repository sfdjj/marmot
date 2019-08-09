#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by wenchao.jia on 19-8-9.
# Mail:wenchao.jia@qunar.com
from pypattyrn.creational.singleton import Singleton

base_url = 'http://127.0.0.1:8080'

URL_SUFFIX = ['message', 'start', 'pre_trigger', 'update']


class TaskService(metaclass=Singleton):

    def __init__(self):
        self.task_dict = {}

    async def create_task(self):
        data = [{'tag': 'A', 'dependencies': []},
                {'tag': 'B', 'dependencies': ['A', 'C']},
                {'tag': 'C', 'dependencies': ['A']},
                {'tag': 'D', 'dependencies': ['B', 'C']}]
        for d in data:
            url = {}
            for url_suffix in URL_SUFFIX:
                url[f'{url_suffix}_url'] = base_url + url_suffix
            d['url'] = url
        print(data)

    async def put_task_dict(self, channel_id, data):
        self.task_dict[channel_id] = data

    async def get_task_dict(self, channel_id):
        return self.task_dict.get(channel_id, {})

    async def rm_task_dict(self, channel_id):
        return self.task_dict.pop(channel_id)


if __name__ == '__main__':
    TaskService().create_task()