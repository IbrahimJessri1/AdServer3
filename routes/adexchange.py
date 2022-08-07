

from pickle import ADDITEMS
from fastapi import APIRouter

from models.adrequest import Ad_Request
from repositries import adexchange as repo_adexchange

adexchange_router = APIRouter(
    prefix="/adexchange",
    tags = ['AdExchange']
)


@adexchange_router('/negotiate')
async def negotiate(request : Ad_Request):
    return repo_adexchange.negotiate(request)
