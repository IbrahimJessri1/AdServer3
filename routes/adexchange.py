

from pickle import ADDITEMS
from fastapi import APIRouter

from models.ssp import Ad_Request
from repositries import adexchange as repo_adexchange

adexchange_router = APIRouter(
    prefix="/adexchange",
    tags = ['AdExchange']
)


@adexchange_router.post('/negotiate')
async def negotiate(request : Ad_Request):
    return repo_adexchange.negotiate(request)
