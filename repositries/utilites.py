
from models.advertisement import Advertisement, Category, MarketingInfo
from pydantic import BaseModel
from enum import Enum
from uuid import UUID
import random


def get_dict(obj):
    res = {}
    for att in dir(obj):
        if att.startswith('__') or att in dir(BaseModel) or att in dir(Enum) or att in dir(str) or att in dir(UUID):
            continue
        value = getattr(obj, att)
        if type(value).__name__ == 'int':
            res[att] = value
        elif type(value).__name__ == 'float':
            res[att] = value
        elif type(value).__name__ == 'list':
            res[att] = value
        elif type(value).__name__ == 'str':
            res[att] = value
        elif issubclass(type(value), UUID):
            res[att] = str(value)
        elif issubclass(type(value), Enum):
            res[att] = value.value
        else:
            res[att] = get_dict(value)
    return res



def probability_get(param):
    sum = 0
    for t in param:
        sum += t[1]
    param.sort(key= lambda x : x[1])
    val = random.uniform(0, sum)
    yet = 0
    for t in param:
        yet += t[1]
        if yet >= val:
            return t[0]
