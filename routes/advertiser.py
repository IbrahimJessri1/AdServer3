from fastapi import APIRouter, status
from models.advertiser import Advertiser
from repositries import advertiser as repo_advertiser



advertiser_router = APIRouter(
    prefix="/advertiser",
    tags = ['Advertiser']
)




@advertiser_router.get('/')
async def get_message():
    return {"message" : "hi"}



@advertiser_router.post('/signup', status_code=status.HTTP_201_CREATED)
async def sign_up(advertiser: Advertiser):
    return repo_advertiser.signup(advertiser)