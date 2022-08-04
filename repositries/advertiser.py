from models.users import Advertiser, AdvertiserShow, Role
from fastapi import HTTPException, status
from config.db import conn
from repositries import generics as gen
from .hashing import Hash



def signup(advertiser : Advertiser):
    try:
        collection = conn.AdServer.user
        user = gen.get_one(collection, {"username" : advertiser.username})
        if user:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="username taken!")
        advertiser.password = Hash.bcrypt(advertiser.password)
        user = dict(advertiser)
        user["role"] = Role.ADVERTISER.value
        collection.insert_one(user)
        inserted = gen.get_one(collection, {"username" : advertiser.username})
        return AdvertiserShow(username = inserted["username"], role = inserted["role"], membership = inserted["membership"])
    except HTTPException as http_excep:
        raise http_excep    
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An Error Happaned, try again later") 

def get_all():
    return gen.get(conn.AdServer.user, {})







