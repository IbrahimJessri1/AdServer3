from sre_parse import CATEGORIES
from uuid import UUID, uuid4
from pydantic import UUID4, BaseModel
from enum import Enum
from typing import List, Optional
from fastapi import UploadFile


class TargetAge(str, Enum):
    ALL_AGES= "all ages"
    KID= "kids"
    YOUTH= "youths"
    ADULT = "adults"
    OLD = "old people"

class Language(str, Enum):
    ANY = "any"
    EN = "en"
    AR = "ar"


class TargetGender(str, Enum):
    BOTH="both"
    MALE= "male"
    FEMALE= "female"


class TargetUserInfo(BaseModel):
    location:str
    gender:TargetGender
    age: TargetAge
    language: Language



class MarketingInfo(BaseModel):
    max_cpc : float
    impressions : int
    clicks: int
    times_served: int
    raise_percentage: float

class AdType(str, Enum):
    TEXT= "text"
    PHOTO= "image"
    VIDEO= "video"
    INTERACTIVE= "interactive"


class AdInfo(BaseModel):
    type : AdType
    advertiser_username: str
    url: str

class Category(str, Enum):
    ANY= "any"
    TECHNOLOGY= "technology"



class AdvertisementInput(BaseModel):
    target_user_info: TargetUserInfo
    max_cpc: float
    type: AdType
    categories: List[Category]
    url:str
    raise_percentage: float

class Advertisement(BaseModel):
    id:Optional[UUID] = uuid4()
    create_date: str
    target_user_info: TargetUserInfo
    marketing_info: MarketingInfo
    ad_info: AdInfo
    categories: List[Category]
