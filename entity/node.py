# Created by wenchao.jia on 2019-06-03.
# Mail:wenchao.jia@qunar.com
from common import TaskPeriodType


class PeriodNode:
    def __init__(self):
        self.period = TaskPeriodType.sleep
        self.next_period_nodes = {}
        self.next_process = TaskExecService.sleep_next_process

    def add_next_node(self, action: ActionType, period_node):
        self.next_period_nodes[action] = period_node

    def get_next_period_by_orch_task_type(self, orch_task_type: TaskType):
        return None

    def get_next_period_by_action(self, action: ActionType):
        return self.next_period_nodes[action].period