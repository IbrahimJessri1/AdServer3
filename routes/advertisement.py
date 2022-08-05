
from fastapi import APIRouter, UploadFile, status, HTTPException, UploadFile, File, Depends
from repositries import oauth2
import shutil
from models.token import TokenData
from models.advertisement import AdvertisementInput
from repositries import advertisement as repo_advertisement


advertisement_router = APIRouter(
    prefix="/advertisement",
    tags = ['Advertisement']
)




@advertisement_router.post('/create_ad',  status_code=status.HTTP_201_CREATED)
async def create_ad(ad_input: AdvertisementInput, file : UploadFile=File(...), current_username : TokenData = Depends(oauth2.get_current_user)):
    #authorize
    return repo_advertisement.create_ad(ad_input, file, current_username.username)