from fastapi import FastAPI

from routes import advertiser


app = FastAPI()


app.include_router(advertiser.advertiser_router)
