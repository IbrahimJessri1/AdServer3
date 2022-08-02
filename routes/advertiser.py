from fastapi import APIRouter
from models.advertiser import Advertiser

advertiser_router = APIRouter(
    prefix="/advertiser",
    tags = ['Advertiser']
)




@advertiser_router.get('/')
async def get_message():
    return {"message" : "hi"}



@advertiser_router.post('/signup')
async def sign_up(advertiser: Advertiser):
    return {"msg" : "nice"}