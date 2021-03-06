# Created by wenchao.jia on 2019-05-31.
# Mail:wenchao.jia@qunar.com
from asyncio import Event
from collections import defaultdict
from typing import List

from server.app.common import StatusType, TaskPeriodType, period_action_map
from server.app.entity import DictObject, BaseEntity


class TaskExec(BaseEntity, DictObject):
    def __init__(self):
        super().__init__()
        self.events = defaultdict(Event)
        self.dependencies = []  # type:List[str]
        self.task_exec_dependencies = []  # type:List[TaskExec]
        self.task_key = ''
        self.status = StatusType.in_process
        self.period = TaskPeriodType.sleep
        self.action = None
        self.tag = None
        self.pipeline_exec = None
        self.workflow = None
        self.start_time = None
        self.end_time = None

    @classmethod
    def create_entity(cls, dict_data: dict):
        instance = cls()
        instance.update_attrs(dict_data)
        return instance

    async def update_period(self, period):
        async with self.lock:
            if period == TaskPeriodType.running:
                print(f'server.app.task{self.tag}开始执行')
            self.action = period_action_map[period]
            from server.service.period_service import PeriodService
            await PeriodService().update_period(self, period)
