# Created by wenchao.jia on 2019-06-03.
# Mail:wenchao.jia@qunar.com
from common import TaskPeriodType


class WorkFlow:
    def __init__(self):
        self.period_nodes = {}

    def get_node(self, period: TaskPeriodType):
        return self.period_nodes[period]


class TaskWorkFlow(WorkFlow):
    def __init__(self):
        super().__init__()

