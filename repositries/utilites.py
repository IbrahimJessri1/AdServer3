
from models.advertisement import Advertisement, Category, MarketingInfo
from pydantic import BaseModel
from enum import Enum
from uuid import UUID
import random
from models.ssp import UserInfo
from models.advertisement import Language, TargetAge

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

def rand(start, end, decimal_places):
    return  round(random.uniform(start, end), decimal_places)


gender_weight = 4
age_weight = 4
language_weight = 4
location_weight = 4



def get_weight_user_info(user_info : UserInfo, ad):
    total_weight = 0
    weight_gained = 0
    if user_info is not None:
            if user_info.gender is not None:
                total_weight += gender_weight
                if user_info.gender.value == ad["target_user_info"]["gender"]:
                    weight_gained += gender_weight
                elif 'both'== ad["target_user_info"]["gender"]:
                    weight_gained += gender_weight/2

            if user_info.age is not None:
                total_weight += age_weight
                if ad["target_user_info"]["age"] == TargetAge.ALL_AGES:
                    weight_gained += age_weight/2
                elif user_info.age <= 12:
                    if ad["target_user_info"]["age"] == TargetAge.KID:
                        weight_gained += age_weight
                elif user_info.age <= 39:
                    if ad["target_user_info"]["age"] == TargetAge.YOUTH:
                        weight_gained += age_weight
                elif user_info.age <= 55:
                    if ad["target_user_info"]["age"] == TargetAge.ADULT:
                        weight_gained += age_weight
                elif user_info.age > 55:
                    if ad["target_user_info"]["age"] == TargetAge.OLD:
                        weight_gained += age_weight
            if user_info.language is not None:
                total_weight += language_weight
                if ad["target_user_info"]["language"] == Language.ANY:
                    weight_gained += language_weight/2
                elif ad["target_user_info"]["language"] == user_info.language:
                    weight_gained += language_weight
            if user_info.location is not None:
                total_weight += location_weight
                if ad["target_user_info"]["location"].lower() == user_info.location.lower():
                    weight_gained += location_weight
                else:
                    weight_gained += location_weight/2
    return [weight_gained, total_weight]