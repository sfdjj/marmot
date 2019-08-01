#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by wenchao.jia on 19-6-10.
# Mail:wenchao.jia@qunar.com

class PeriodIllegalException(Exception):
    status, title = 1002, '更新的状态不合法'


class NoPipelineExecException(Exception):
    status, title = 1003, 'pipeline_exec不存在'
