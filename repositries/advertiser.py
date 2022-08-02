
from models.advertiser import Advertiser
from fastapi import HTTPException, status



def signup(advertiser : Advertiser):
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"no signup for u") 