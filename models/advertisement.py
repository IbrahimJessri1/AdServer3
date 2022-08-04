from sre_parse import CATEGORIES
from pydantic import BaseModel
from enum import Enum
from typing import List

class TargetAge(str, Enum):
    ALL_AGES= "all ages"
    KID= "kids"
    TEEN= "teens"
    ADULT = "adults"
    OLD = "old people"

class Language(str, Enum):
    EN = "en"
    AR = "ar"


class TargetGender(str, Enum):
    MALE= "male"
    FEMALE= "female"
    BOTH="both"


class TargetUserInfo(BaseModel):
    location:str
    gender:TargetGender
    age: TargetAge
    language: Language



class MarketingInfo(BaseModel):
    max_cpc : float
    min_cpc : float

class AdType(str, Enum):
    TEXT= "text"
    PHOTO= "photo"
    VIDEO= "video"
    INTERACTIVE= "interactive"


class AdInfo(BaseModel):
    filename: str
    path : str
    type : AdType
    advertiser_username: str


class Category(str, Enum):
    TECHNOLOGY= "technology"



class AdvertisementInput(BaseModel):
    target_user_info: TargetUserInfo
    marketing_info: MarketingInfo
    type: AdType
    categories: List[Category]


class Advertisement(BaseModel):
    id:int
    target_user_info: TargetUserInfo
    marketing_info: MarketingInfo
    ad_info: AdInfo
    categories: List[Category]



