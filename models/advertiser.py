from lib2to3.pytree import Base
from pydantic import BaseModel
from enum import Enum


class Membership(Enum):
    NORMAL = 0.2
    PREMIUM = 0.35
    VIP = 0.45


class Advertiser(BaseModel):
    username: str
    email:str
    password:str
    membership:Membership

