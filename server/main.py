# Created by wenchao.jia on 2019-05-31.
# Mail:wenchao.jia@qunar.com
import asyncio
import uvloop

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
from server.app.service.pipeline_exec_registery import PipelineExecRegistry


async def test():
    data = [{'tag': 'A', 'dependencies': []},
            {'tag': 'B', 'dependencies': ['A', 'C']},
            {'tag': 'C', 'dependencies': ['A']},
            {'tag': 'D', 'dependencies': ['B', 'C']}]

    PipelineExecRegistry().init_pipeline(data)


if __name__ == '__main__':
    asyncio.run(test())
