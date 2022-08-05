from fastapi import FastAPI

from routes import advertiser, authentication, advertisement, user


app = FastAPI()


app.include_router(advertiser.advertiser_router)
app.include_router(authentication.authentication_router)
app.include_router(advertisement.advertisement_router)
app.include_router(user.user_router)