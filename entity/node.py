# Created by wenchao.jia on 2019-06-03.
# Mail:wenchao.jia@qunar.com
from common import TaskPeriodType, ActionType
from service.task_exec_service import TaskExecService


class PeriodNode:
    def __init__(self):
        self.period = TaskPeriodType.sleep
        self.next_period_nodes = {}
        self.next_process = TaskExecService.sleep_next_process

    def add_next_node(self, action: ActionType, period_node):
        self.next_period_nodes[action] = period_node

    def get_next_period_by_action(self, action: ActionType):
        return self.next_period_nodes[action].period


class SleepNode(PeriodNode):
    def __init__(self):
        super().__init__()
        self.period = TaskPeriodType.sleep
        self.next_process = TaskExecService.sleep_next_process


class SuccessNode(PeriodNode):
    def __init__(self):
        super().__init__()
        self.period = TaskPeriodType.success
        self.next_periods = {}
        self.next_process = {}


class FailureNode(PeriodNode):
    def __init__(self):
        super().__init__()
        self.period = TaskPeriodType.failure
        self.next_periods = {}
        self.next_process = None


class SystemStopNone(PeriodNode):
    def __init__(self):
        super().__init__()
        self.period = TaskPeriodType.system_stop
        self.next_periods = {}
        self.next_process = None


class UserStopNode(PeriodNode):
    def __init__(self):
        super().__init__()
        self.period = TaskPeriodType.user_stop
        self.next_periods = {}
        self.next_process = None


class TimeoutNode(PeriodNode):
    def __init__(self):
        super().__init__()
        self.period = TaskPeriodType.timeout
        self.next_periods = {}
        self.next_process = None


class LossNode(PeriodNode):
    def __init__(self):
        super().__init__()
        self.period = TaskPeriodType.loss
        self.next_periods = {}
        self.next_process = None


class CancelNode(PeriodNode):
    def __init__(self):
        super().__init__()
        self.period = TaskPeriodType.cancel
        self.next_process = None


class SkippedNode(PeriodNode):
    def __init__(self):
        super().__init__()
        self.period = TaskPeriodType.skipped
        self.next_process = None


class RunningNode(PeriodNode):
    def __init__(self):
        super().__init__()
        self.period = TaskPeriodType.running
        self.next_periods = {
            ActionType.system_stop: SystemStopNone(),
            ActionType.receive_fail: FailureNode(),
            ActionType.user_stop: UserStopNode(),
            ActionType.receive_success: SuccessNode(),
            ActionType.timeout: TimeoutNode(),
        }
        self.next_process = TaskExecService.wait_message


class WaitNode(PeriodNode):
    def __init__(self):
        super().__init__()
        self.period = TaskPeriodType.waiting
        self.next_process = TaskExecService.trigger_task_start
