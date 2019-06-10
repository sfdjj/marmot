# Created by wenchao.jia on 2019-06-03.
# Mail:wenchao.jia@qunar.com
from pydash import filter_

from common import TaskPeriodType, StatusType, FAIL_STATUS, ActionType
from task import TaskExec


class TaskExecService:
    @classmethod
    async def trigger_task_start(cls, task_exec: TaskExec):
        async with task_exec.lock:
            print(f'开始执行{task_exec.tag}')

    @classmethod
    async def wait_message(cls, task_exec: TaskExec):
        print(f'task_exec{task_exec}当前状态{TaskPeriodType(task_exec.period).phrase}')
        await task_exec.events[task_exec.period].wait()

    @staticmethod
    async def sleep_next_process(task_exec: TaskExec):
        for dependency in task_exec.task_exec_dependencies:
            async with dependency.finished:
                await dependency.finished.wait_for(lambda: dependency['status'] != StatusType.in_process)

        async with task_exec.lock:
            if filter_(task_exec.task_exec_dependencies, lambda x: x['status'] in FAIL_STATUS):
                task_exec.action = ActionType.dependency_failure
            else:
                task_exec.action = ActionType.ready

            period = task_exec.workflow.get_node(task_exec.period).get_next_period_by_action(task_exec.action)
