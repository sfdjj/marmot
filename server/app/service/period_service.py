# Created by wenchao.jia on 2019-06-03.
# Mail:wenchao.jia@qunar.com
from pydash import pluck

from server.app.common import TaskPeriodType, StatusType, START_PERIOD, END_PERIOD, period_status_map
from server.app.common.exception import PeriodIllegalException
from server.app.service import BaseService
from server.app.task import TaskExec
import datetime


class PeriodService(BaseService):
    async def update_period(self, task_exec: TaskExec, period):
        print(f'{task_exec.tag}更新period为{TaskPeriodType(period).phrase},更新前状态{TaskPeriodType(task_exec.period).phrase}')
        if period not in pluck(task_exec.workflow.get_node(task_exec.period).next_period_nodes, 'period'):
            raise PeriodIllegalException(f'{task_exec}不允许将状态从{task_exec.period}修改为{period}')
        assert task_exec.lock.locked()
        last_period = task_exec.period

        if period in START_PERIOD:
            task_exec.start_time = datetime.datetime.now()
        elif period in END_PERIOD:
            task_exec.end_time = datetime.datetime.now()

        if not task_exec.workflow.get_node(period).next_process:
            status = period_status_map[period]
        else:
            status = task_exec.status
        print(f'task_exec:{task_exec.tag}状态变更,period:{TaskPeriodType(period).phrase},更新前状态{TaskPeriodType(task_exec.period).phrase},status:{StatusType(status)}')
        task_exec.period = period

        if not task_exec.workflow.get_node(period).next_process:
            task_exec.status = period_status_map[period]
            self.logger.info(f'{task_exec}执行结束')
            await task_exec.finished.acquire()
            task_exec.finished.notify_all()
            task_exec.finished.release()

        task_exec.events[last_period].set()
