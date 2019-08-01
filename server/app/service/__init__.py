# Created by wenchao.jia on 2019-06-03.
# Mail:wenchao.jia@qunar.com\
import logging


class BaseService:
    logger_name = 'app'

    def __init__(self):
        self.logger = logging.getLogger(self.logger_name)
