from fastapi import FastAPI
from pydantic import BaseModel
from routes import advertiser, authentication, advertisement, user, adexchange, serve_ads
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")



app.include_router(advertiser.advertiser_router)
app.include_router(authentication.authentication_router)
app.include_router(advertisement.advertisement_router)
app.include_router(user.user_router)
app.include_router(adexchange.adexchange_router)
app.include_router(serve_ads.serve_ads_router)


