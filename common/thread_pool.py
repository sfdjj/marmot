#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by wenchao.jia on 19-7-30.
# Mail:wenchao.jia@qunar.com
import asyncio
import functools
import inspect
import threading
from concurrent.futures.thread import ThreadPoolExecutor

MAX_THREAD_WORKER = 20
executor = ThreadPoolExecutor(MAX_THREAD_WORKER, 'Thread')


def on_executor(func):
    assert not inspect.iscoroutinefunction(func)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        assert threading.current_thread() is threading.main_thread()
        return asyncio.get_event_loop().run_in_executor(executor, lambda: func(*args, **kwargs))

    return wrapper
