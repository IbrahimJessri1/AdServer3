from pydantic import BaseModel
from enum import Enum


class Membership(Enum):
    NORMAL = "NORMAL" #0.2
    PREMIUM = "PREMIUM" #0.35
    VIP = "VIP" #0.45


class Advertiser(BaseModel):
    username: str
    email:str
    password:str
    membership:Membership

