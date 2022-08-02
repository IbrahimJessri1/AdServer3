from fastapi import APIRouter


advertiser_router = APIRouter(
    prefix="/advertiser"
)




@advertiser_router.get('/')
async def get_message():
    return {"message" : "hi"}



