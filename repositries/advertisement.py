import shutil
from uuid import uuid4
from fastapi import HTTPException, status
from config.db import conn
from repositries import generics as gen
from models.advertisement import AdInfo, Advertisement
import datetime

def create_ad(ad_input, file, advertiser_username):
    try:
        create_date = str(datetime.datetime.now())
        id = uuid4()
        path = 'advertisements/' + advertiser_username + str(id)
        with open(path, 'wb') as buffer:
            shutil.copyfileobj(file.file, buffer)
        ad_info = AdInfo(type = ad_input.type, advertiser_username=advertiser_username, path=path)
        advertisement = Advertisement(
            id = id,
            create_date = create_date, 
            target_user_info=ad_input.target_user_info, 
            marketing_info=ad_input.marketing_info,
            ad_info = ad_info,
            categories=ad_input.categories
        )
        return ad_info
    except:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail='An error happened, try again later')