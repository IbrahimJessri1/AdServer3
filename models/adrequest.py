from pydantic import BaseModel
from enum import Enum
from typing import Optional, List


class Gender(str, Enum):
    MALE= "male"
    FELMALE= "female"

class Age(str, Enum):
    KID= "kids"
    TEEN= "teens"
    ADULT = "adults"
    OLD = "old people"


class Language(str, Enum):
    EN= "en"
    AR = "ar"


class UserInfo(BaseModel):
    location: Optional[str] = None
    gender: Optional[Gender] = None
    age: Optional[Age] = None
    language: Optional[Language] = None

    
class Category(str, Enum):
    TECHNOLOGY= "technology"

class Categories(BaseModel):
    categories_list: Optional[List[Category]] = None


class Ad_Request(BaseModel):
    min_cpc: float
    user_info: Optional[UserInfo] = None
    categories: Optional[Categories] = None