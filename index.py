from fastapi import FastAPI

from routes import advertiser, authentication


app = FastAPI()


app.include_router(advertiser.advertiser_router)
app.include_router(authentication.authentication_router)
