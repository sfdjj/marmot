# Created by wenchao.jia on 2019-06-03.
# Mail:wenchao.jia@qunar.com
from asyncio import CancelledError

from common import END_STATUS
from task import TaskExec


class TriggerService:
    async def start_forever(self, task_exec: TaskExec):
        try:
            while task_exec.status not in END_STATUS:
                period_node = task_exec.workflow.get_node(task_exec.period)  # type:PeriodNode
                await period_node.next_process(task_exec)
        except CancelledError:
            print(f'{task_exec}所在的asyncio_task cancel成功')
