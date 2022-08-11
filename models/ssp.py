from unicodedata import category
from pydantic import BaseModel
from enum import Enum
from typing import Optional, List

from models.advertisement import AdType


class Gender(str, Enum):
    MALE= "male"
    FELMALE= "female"




class Language(str, Enum):
    EN= "en"
    AR = "ar"


class UserInfo(BaseModel):
    location: Optional[str] = None
    gender: Optional[Gender] = None
    age: Optional[int] = None
    language: Optional[Language] = None

    
class Category(str, Enum):
    TECHNOLOGY= "technology"

class Categories(BaseModel):
    categories_list: List[Category]



class Ad_Request(BaseModel):
    min_cpc: float
    user_info: Optional[UserInfo] = None
    categories: Optional[Categories] = None
    type: AdType
    keywords: Optional[List[str]] = None


class ApplyAd(BaseModel):
    cpc: float
    ad_id: str