from config.db import conn
from models.users import UserShow
from repositries import generics as gen
from .hashing import Hash
from fastapi import HTTPException, status

def get_all():
    return gen.get_many(conn.AdServer.user, {})


def remove(constraints):
    gen.remove(conn.AdServer.user, constraints)





def update_account(user_update, username):
    try:
        query = { "username": username}
        in_values = {}
        in_values["password"] = Hash.bcrypt(user_update.password)
        new_values = { "$set": in_values }
        res = gen.update_one(conn.AdServer.user, query, new_values)
        return UserShow(username=res["username"], role=res["role"], create_date=res["create_date"])
    except HTTPException as http_excep:
        raise http_excep    
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An Error Happaned, try again later") 


def delete_account(username):
    gen.remove(conn.AdServer.user, {"username" : username})



def get(username):
    try:
        res = gen.get_one(conn.AdServer.user, {"username" : username})
        return UserShow(username=res["username"], role=res["role"], create_date=res["create_date"])
    except HTTPException as http_excep:
        raise http_excep    
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An Error Happaned, try again later") 