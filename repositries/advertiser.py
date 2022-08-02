
from models.advertiser import Advertiser
from fastapi import HTTPException, status
from config.db import conn
from schemas.base_schema import serializeList,serializeDict
import pymongo


def signup(advertiser : Advertiser):
    try:
        user = get_by_username(advertiser.username)
        if not user:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="An Error Happaned, try again later") 
        conn.AdServer.advertiser.insert_one(dict(advertiser))
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An Error Happaned, try again later") 
    return serializeList(conn.AdServer.advertiser.find())


def get_by_username(usr : str):
    try:
        return serializeDict(conn.AdServer.advertiser.find({"username" : usr}))
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An Error Happaned, try again later") 
    


def get_all():
    try:
        return serializeList(conn.AdServer.advertiser.find())
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An Error Happaned, try again later") 