# Created by wenchao.jia on 2019-05-31.
# Mail:wenchao.jia@qunar.com
from typing import List

import networkx
from networkx import OrderedDiGraph

from entity import BaseEntity
from task import TaskExec


class PipelineExec(BaseEntity):
    def __init__(self):
        super().__init__()
        self.system_code = ''
        self.task_execs = []  # type:List[TaskExec]
        self.build_network = OrderedDiGraph()

    def add_task_exec(self, task_exec: TaskExec):
        self.task_execs.append(task_exec)
        task_exec.pipeline_exec = self
        return self

    def check_circle(self):
        try:
            edges = networkx.find_cycle(self.build_network)
        except networkx.NetworkXNoCycle:
            pass
        else:
            raise Exception(f"存在依赖循环:{edges}")
