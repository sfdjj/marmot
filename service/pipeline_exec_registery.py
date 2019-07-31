#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by wenchao.jia on 19-7-30.
# Mail:wenchao.jia@qunar.com
import asyncio

from pydash import key_by
from pypattyrn.creational.singleton import Singleton

from common import END_PERIOD
from common.exception import NoPipelineExecException
from pipeline import PipelineExec
from service.trigger_service import TaskExecTriggerService
from task import TaskExec


class PipelineExecRegistry(metaclass=Singleton):
    def __init__(self):
        self.pipeline_execs = {}

    def init_pipeline(self, data):
        pipeline_exec = PipelineExec()
        for task in data:
            task_exec = TaskExec().create_entity(task)
            from entity.workflow import TaskWorkFlow
            task_exec.workflow = TaskWorkFlow()
            pipeline_exec.add_task_exec(task_exec)

        task_exec_dict = key_by(pipeline_exec.task_execs, 'tag')

        for task_exec in pipeline_exec.task_execs:
            for dependency in task_exec.dependencies:
                task_exec.task_exec_dependencies.append(task_exec_dict[dependency])

        pipeline_exec.build_network.add_nodes_from(pipeline_exec.task_execs)

        for task_exec in pipeline_exec.task_execs:
            for task_exec_dependency in task_exec.task_exec_dependencies:
                pipeline_exec.build_network.add_edge(task_exec, task_exec_dependency)
            if task_exec.period not in END_PERIOD:
                # 启动task
                print(f'启动task:{task_exec.tag}')
                asyncio_task = asyncio.get_event_loop().create_task(
                    TaskExecTriggerService().start_forever(task_exec))
                task_exec.asyncio_task = asyncio_task

        asyncio.sleep(5)
        pipeline_exec.check_circle()

    def get_pipeline_exec(self, system_code):
        pipeline = self.pipeline_execs.get(system_code)
        if not pipeline:
            raise NoPipelineExecException(f'system_code={system_code}的pipeline_exec不存在')
        return pipeline

    def remove(self, pipeline_exec: PipelineExec):
        self.pipeline_execs.pop(pipeline_exec.system_code)

    def __register(self, pipeline_exec: PipelineExec):
        self.pipeline_execs[pipeline_exec.system_code] = pipeline_exec
