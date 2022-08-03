
from fastapi import HTTPException, status
from schemas.base_schema import serializeDict, serializeList


def get(collection, constraints : dict):
    try:
        return serializeList(collection.find(constraints))
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An Error Happaned, try again later") 


def get_one(collection, constraints : dict):
    try:
        res =collection.find_one(constraints)
        if res is None:
            return {}
        return serializeDict(res)
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail= "An Error Happaned, try again later") 




def remove(collection, constraints):
    try:
        collection.delete_many(constraints)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail= e.detail) 