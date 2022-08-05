import shutil
from tempfile import gettempdir
from uuid import uuid4
from fastapi import HTTPException, status
from config.db import conn
from repositries import generics as gen
from models.advertisement import AdInfo, Advertisement
import datetime
from .utilites import get_dict

def create_ad(ad_input, advertiser_username):
    try:
        create_date = str(datetime.datetime.now())
        ad_info = AdInfo(type = ad_input.type, advertiser_username=advertiser_username, url=ad_input.url)
        advertisement = Advertisement(
            create_date = create_date,
            target_user_info=ad_input.target_user_info, 
            marketing_info=ad_input.marketing_info,
            ad_info= ad_info,
            categories=ad_input.categories
        )
        d = get_dict(advertisement)
        conn.AdServer.advertisement.insert_one(dict(d))
    except:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail='An error happened, try again later')


##admin uses
def get_all():
    return gen.get_many(conn.AdServer.advertisement, {})



