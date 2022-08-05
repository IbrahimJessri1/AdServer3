from sre_parse import CATEGORIES
from uuid import UUID, uuid4
from pydantic import UUID4, BaseModel
from enum import Enum
from typing import List, Optional

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
    type : AdType
    advertiser_username: str
    path: str

class Category(str, Enum):
    TECHNOLOGY= "technology"



class AdvertisementInput(BaseModel):
    target_user_info: TargetUserInfo
    marketing_info: MarketingInfo
    type: AdType
    categories: List[Category]


class Advertisement(BaseModel):
    id:Optional[UUID] = uuid4()
    create_date: str
    target_user_info: TargetUserInfo
    marketing_info: MarketingInfo
    ad_info: AdInfo
    categories: List[Category]


