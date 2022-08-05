
from fastapi import APIRouter, UploadFile, status, HTTPException, UploadFile, File, Depends
from repositries import oauth2
import shutil
from models.token import TokenData
from models.advertisement import AdvertisementInput
from repositries import advertisement as repo_advertisement
from repositries.validation import Validator
from typing import Optional
import json
advertisement_router = APIRouter(
    prefix="/advertisement",
    tags = ['Advertisement']
)




@advertisement_router.post('/create_ad',)#  status_code=status.HTTP_204_NO_CONTENT)
async def create_ad(ad_input:AdvertisementInput, current_username : TokenData = Depends(oauth2.get_current_user)):
    #authorize  
    if not Validator.validate(ad_input):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='make sure of request arguments')
    repo_advertisement.create_ad(ad_input, current_username.username)



#admin
@advertisement_router.get('/')
async def get_all():
    return repo_advertisement.get_all()