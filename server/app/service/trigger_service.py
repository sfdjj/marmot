# Created by wenchao.jia on 2019-06-03.
# Mail:wenchao.jia@qunar.com
from asyncio import CancelledError

from server.app.common import END_STATUS
from server.app.entity.node import PeriodNode
from server.app.task import TaskExec


class TaskExecTriggerService:
    async def start_forever(self, task_exec: TaskExec):
        print(f'开始调度:{task_exec.tag}')
        try:
            while task_exec.status not in END_STATUS:
                period_node = task_exec.workflow.get_node(task_exec.period)  # type:PeriodNode
                await period_node.next_process(task_exec)
        except CancelledError:
            print(f'{task_exec}所在的asyncio_task cancel成功')
