# Created by wenchao.jia on 2019-06-03.
# Mail:wenchao.jia@qunar.com
from entity.node import *


class WorkFlow:
    def __init__(self):
        self.period_nodes = {}

    def get_node(self, period: TaskPeriodType):
        return self.period_nodes[period]


class TaskWorkFlow(WorkFlow):
    def __init__(self):
        super().__init__()
        sleep_node = SleepNode()
        success_node = SuccessNode()
        failure_node = FailureNode()
        system_stop_node = SystemStopNone()
        user_stop_node = UserStopNode()
        timeout_node = TimeoutNode()
        running_node = RunningNode()
        waiting_node = WaitNode()
        cancel_node = CancelNode()
        skipped_node = SkippedNode()

        sleep_node.add_next_node(ActionType.ready, waiting_node)
        sleep_node.add_next_node(ActionType.user_stop, user_stop_node)
        sleep_node.add_next_node(ActionType.dependency_failure, cancel_node)
        waiting_node.add_next_node(ActionType.skip, skipped_node)
        waiting_node.add_next_node(ActionType.start_fail, failure_node)
        waiting_node.add_next_node(ActionType.user_stop, user_stop_node)
        waiting_node.add_next_node(ActionType.system_stop, system_stop_node)
        waiting_node.add_next_node(ActionType.timeout, timeout_node)
        waiting_node.add_next_node(ActionType.receive_start, running_node)
        running_node.add_next_node(ActionType.receive_success, success_node)
        running_node.add_next_node(ActionType.fail, failure_node)
        running_node.add_next_node(ActionType.user_stop, user_stop_node)
        running_node.add_next_node(ActionType.system_stop, system_stop_node)
        running_node.add_next_node(ActionType.timeout, timeout_node)
        self.period_nodes = {
            TaskPeriodType.sleep: sleep_node,
            TaskPeriodType.waiting: waiting_node,
            TaskPeriodType.running: running_node,
            TaskPeriodType.success: success_node,
            TaskPeriodType.skipped: skipped_node,
            TaskPeriodType.user_stop: user_stop_node,
            TaskPeriodType.failure: failure_node,
            TaskPeriodType.system_stop: system_stop_node,
            TaskPeriodType.cancel: cancel_node,
            TaskPeriodType.timeout: timeout_node
        }
