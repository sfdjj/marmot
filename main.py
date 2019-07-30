# Created by wenchao.jia on 2019-05-31.
# Mail:wenchao.jia@qunar.com
import asyncio

from pydash import key_by

from common import END_PERIOD
from pipeline import PipelineExec
from service.trigger_service import TaskExecTriggerService
from task import TaskExec

data = [{'tag': 'A', 'dependencies': []},
        {'tag': 'B', 'dependencies': ['A', 'C']},
        {'tag': 'C', 'dependencies': ['A']},
        {'tag': 'D', 'dependencies': ['B', 'C']}]

pipeline_exec = PipelineExec()

for task in data:
    task_exec = TaskExec().create_entity(task)
    pipeline_exec.add_task_exec(task_exec)

task_exec_dict = key_by(pipeline_exec.task_execs, 'tag')

for task_exec in pipeline_exec.task_execs:
    for dependency in task_exec.dependencies:
        task_exec.task_exec_dependencies.append(task_exec_dict[dependency])

pipeline_exec.build_network.add_nodes_from(pipeline_exec.task_execs)

for task_exec in pipeline_exec.task_execs:
    for task_exec_dependency in task_exec.task_exec_dependencies:
        pipeline_exec.build_network.add_edge(task_exec, task_exec_dependency)
    if task_exec.period not in END_PERIOD:
        # 启动task
        print(f'启动task:{task_exec.tag}')
        asyncio_task = asyncio.get_event_loop().create_task(
            TaskExecTriggerService().start_forever(task_exec))
        task_exec.asyncio_task = asyncio_task

pipeline_exec.check_circle()
