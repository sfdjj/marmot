# Created by wenchao.jia on 2019-05-31.
# Mail:wenchao.jia@qunar.com
import asyncio

from pydash import omit


class DictObject:
    def __init__(self):
        super().__init__()

    def __getitem__(self, item):
        return self.__getattribute__(item)

    def __setitem__(self, key, value):
        self.__setattr__(key, value)

    def update_attrs(self, dict_data: dict):
        for key, value in dict_data.items():
            self.__setattr__(key, value)

    @property
    def dict(self):
        return omit(self.__dict__.copy(), 'lock')

    @classmethod
    def create_entity(cls, dict_data: dict):
        instance = cls()
        instance.update_attrs(dict_data)
        return instance

    @classmethod
    def create_entities(cls, dict_list: list):
        return [cls.create_entity(dict_data) for dict_data in dict_list]


class BaseEntity(DictObject):
    fields = []

    def __init__(self):
        super().__init__()
        self.lock = asyncio.Lock()
        self.finished = asyncio.Condition()
        self._init_attrs()

    def _init_attrs(self):
        pass

    def __getitem__(self, item):
        return self.__getattribute__(item)

    def __setitem__(self, key, value):
        self.__setattr__(key, value)

    def to_dict(self):
        return self.dict
