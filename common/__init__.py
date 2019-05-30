# Created by wenchao.jia on 2019-05-31.
# Mail:wenchao.jia@qunar.com
from enum import IntEnum, unique
from typing import Type


@unique
class StatusType(IntEnum):
    # 未完成
    in_process = -1
    # 成功
    success = 0
    # 终止
    stop = 1
    # 失败
    failure = 2


@unique
class TaskPeriodType(IntEnum):
    def __new__(cls: Type[int], value: int, phrase):
        obj = int.__new__(cls, value)
        obj._value_ = value

        obj.phrase = phrase
        return obj

    sleep = 1, '初始化'
    waiting = 2, '排队中1'
    running = 3, '运行中'
    success = 4, '正常结束'
    loss = 5, '失联'
    timeout = 6, '等待超时'
    user_stop = 7, '用户终止'
    system_stop = 8, '系统终止'
    cancel = 9, '取消'
    failure = 10, '异常结束'
    skipped = 11, '跳过执行'


@unique
class ActionType(IntEnum):
    ready = 1
    receive_start = 2
    receive_success = 3
    receive_fail = 4
    run_jenkins = 5
    run_normal = 6
    user_stop = 7
    dependency_failure = 8
    finish = 9
    fail = 10
    system_stop = 11
    skip = 12
    timeout = 13
    start_fail = 14


period_action_map = {
    TaskPeriodType.running: ActionType.receive_start,
    TaskPeriodType.success: ActionType.receive_success,
    TaskPeriodType.failure: ActionType.receive_fail
    # TaskPeriodType.user_stop: ActionType.user_stop
}

period_status_map = {
    TaskPeriodType.success: StatusType.success,
    TaskPeriodType.failure: StatusType.failure,
    TaskPeriodType.user_stop: StatusType.stop,
    TaskPeriodType.skipped: StatusType.success,
    TaskPeriodType.cancel: StatusType.failure,
    TaskPeriodType.timeout: StatusType.failure
}
