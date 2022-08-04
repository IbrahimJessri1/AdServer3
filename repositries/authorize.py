from config.db import conn
from . import generics as gen
from fastapi import HTTPException, status

class Authorize:
    def auth(permission, username):
        role = gen.get_one(conn.AdServer.user, {"username" : username})["role"]
        role_permissions = gen.get_one(conn.AdServer.role_permission, {"role" : role})
        if(role_permissions and (permission in role_permissions["permissions"])):
            return
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="UNAUTHORIZED") 
