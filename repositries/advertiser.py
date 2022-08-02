
from numpy import empty
from models.advertiser import Advertiser
from fastapi import HTTPException, status
from config.db import conn
from schemas.base_schema import serializeList,serializeDict


def signup(advertiser : Advertiser):
    try:
        user = get_by_username(advertiser.username)
        if user is not None:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="username taken!")
        conn.AdServer.advertiser.insert_one(dict(advertiser))
        return get_by_username(advertiser.username)
    except HTTPException as e:
        return e
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An Error Happaned, try again later") 

######## no httpexceptoin cuz no router uses this
def get_by_username(usr : str):
    try:
        res =conn.AdServer.advertiser.find_one({"username" : usr})
        if res is None:
            return None
        return serializeDict(res)
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An Error Happaned, try again later") 
    


def get_all():
    try:
        return serializeList(conn.AdServer.advertiser.find())
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An Error Happaned, try again later") 


def remove_all():
    try:
        conn.AdServer.advertiser.delete_many({})
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An Error Happaned, try again later") 