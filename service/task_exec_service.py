# Created by wenchao.jia on 2019-06-03.
# Mail:wenchao.jia@qunar.com
from task import TaskExec


class TaskExecService:
    @classmethod
    async def trigger_task_start(cls, task_exec: TaskExec):
        async with task_exec.lock:
            print(f'开始执行{task_exec.tag}')
