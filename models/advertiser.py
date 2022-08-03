from msilib.schema import AdvtExecuteSequence
from pydantic import BaseModel
from enum import Enum


class Membership(str, Enum):
    NORMAL = "NORMAL" #0.2
    PREMIUM = "PREMIUM" #0.35
    VIP = "VIP" #0.45


class Advertiser(BaseModel):
    username: str
    password:str
    membership:Membership


class AdvertiserShow(BaseModel):
    username: str
    membership: Membership
    def Print(self):
        print(self.username, self.membership)





