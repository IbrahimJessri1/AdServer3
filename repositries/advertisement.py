import shutil
from tempfile import gettempdir
from uuid import uuid4
from fastapi import HTTPException, status
from config.db import conn
from repositries import generics as gen
from models.advertisement import AdInfo, Advertisement
import datetime
from .utilites import get_dict
import requests
import os



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
        if ad_input.type.value == 'text':
            filename = str(advertisement.id) + '.txt'
            dir = 'advertisements/' + advertiser_username
            download_file(advertisement.ad_info.url, dir, filename)
        if ad_input.type.value == 'image':
            filename = str(advertisement.id) + '.jpg'
            dir = 'advertisements/' + advertiser_username
            download_file(advertisement.ad_info.url, dir, filename)
        if ad_input.type.value == 'video':
            filename = str(advertisement.id) + '.mp4'
            dir = 'advertisements/' + advertiser_username
            download_file(advertisement.ad_info.url, dir, filename)

        d = get_dict(advertisement)
        conn.AdServer.advertisement.insert_one(dict(d))
    except:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail='An error happened, try again later')


##admin uses
def get_all():
    return gen.get_many(conn.AdServer.advertisement, {})



def download_file(URL, dir, filename):
    os.makedirs(dir, exist_ok=True) 
    path = dir + "/" + filename
    response = requests.get(URL)
    open(path, "wb").write(response.content)