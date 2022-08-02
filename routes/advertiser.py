from fastapi import APIRouter


advertiser_router = APIRouter(

)




@advertiser_router.get('/')
async def get_message():
    return {"message" : "hi"}



