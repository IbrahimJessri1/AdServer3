from fastapi import APIRouter, status, Depends
from models.token import TokenData
from models.users import Advertiser, Membership
from repositries import advertiser as repo_advertiser, generics as gen, oauth2
from config.db import conn
from repositries.authorize import Authorize

advertiser_router = APIRouter(
    prefix="/advertiser",
    tags = ['Advertiser']
)


@advertiser_router.get('/')
async def get(current_username : TokenData = Depends(oauth2.get_current_user)):
    #Authorize.auth("get_advertiser", current_username.username)
    return repo_advertiser.get_all()



@advertiser_router.post('/signup', status_code=status.HTTP_201_CREATED)
async def sign_up(advertiser: Advertiser):
    return repo_advertiser.signup(advertiser)


@advertiser_router.put('/membership')
async def update_memebership(membership : Membership, current_username : TokenData = Depends(oauth2.get_current_user)):
    #Authorize.auth("self_membership_update", current_username)
    return repo_advertiser.update_membership(membership, current_username.username)

@advertiser_router.delete('/remove', status_code=status.HTTP_204_NO_CONTENT)
async def remove(constraints : dict, current_username : str = Depends(oauth2.get_current_user)):
    return gen.remove(conn.AdServer.advertiser, constraints)