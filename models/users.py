from typing import List
from pydantic import BaseModel
from enum import Enum


class Membership(str, Enum):
    NORMAL = "NORMAL" #0.2
    PREMIUM = "PREMIUM" #0.35
    VIP = "VIP" #0.45


class Role(str, Enum):
    ADVERTISER = "advertiser"
    ADMIN = "admin"

class User(BaseModel):
    username: str
    password:str
    role: Role
    create_date: str


class UserShow(BaseModel):
    username: str
    role : Role
    create_date:str

class Admin(User):
    pass


class Advertiser(BaseModel):
    username: str
    password:str
    membership:Membership


class AdvertiserShow(BaseModel):
    username: str
    role : Role
    membership: Membership




