from tkinter import EXCEPTION
from models.advertiser import Advertiser
from fastapi import HTTPException, status
from config.db import conn
from schemas.base_schema import serializeList,serializeDict


def signup(advertiser : Advertiser):
    try:
        user = get_one({"username" : advertiser.username})
        if user:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="username taken!")
        
        conn.AdServer.advertiser.insert_one(dict(advertiser))
        return get_one({"username" : advertiser.username})
    except HTTPException as http_excep:
        raise http_excep    
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An Error Happaned, try again later") 

######## no httpexceptoin cuz no router uses this


def get_all():
    return get({})



def get(constraints : dict):
    try:
        return serializeList(conn.AdServer.advertiser.find(constraints))
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An Error Happaned, try again later") 

def get_one(constraints : dict):
    try:
        res =conn.AdServer.advertiser.find_one(constraints)
        if res is None:
            return {}
        return serializeDict(res)
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail= "An Error Happaned, try again later") 


def remove(constraints):
    try:
        conn.AdServer.advertiser.delete_many(constraints)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail= e.detail) 