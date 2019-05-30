# Created by wenchao.jia on 2019-05-31.
# Mail:wenchao.jia@qunar.com
from asyncio import Event
from collections import defaultdict

from common import StatusType, TaskPeriodType, period_action_map
from entity import DictObject, BaseEntity


class TaskExec(BaseEntity, DictObject):
    def __init__(self, tag):
        super().__init__()
        self.events = defaultdict(Event)
        self.dependencies = []
        self.status = StatusType.in_process
        self.period = TaskPeriodType.sleep
        self.action = None
        self.tag = tag

    async def update_period(self, period):
        async with self.lock:
            if period == TaskPeriodType.running:
                print(f'task{self.tag}开始执行')
            self.action = period_action_map[period]
