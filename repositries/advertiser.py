from models.advertiser import Advertiser
from fastapi import HTTPException, status
from config.db import conn
from repositries import generics as gen

def signup(advertiser : Advertiser):
    try:
        collection = conn.AdServer.advertiser
        user = gen.get_one(collection, {"username" : advertiser.username})
        if user:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="username taken!")
        
        conn.AdServer.advertiser.insert_one(dict(advertiser))
        return gen.get_one(collection, {"username" : advertiser.username})
    except HTTPException as http_excep:
        raise http_excep    
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An Error Happaned, try again later") 

def get_all():
    return gen.get(conn.advertiser.advertiser, {})







