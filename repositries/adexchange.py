from fastapi import HTTPException, status
from config.db import conn
from repositries import generics as gen
from models.adrequest import Ad_Request

def negotiate(request : Ad_Request):
    return 'hi'