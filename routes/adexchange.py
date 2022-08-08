from fastapi import APIRouter
from models.ssp import Ad_Request
from repositries import adexchange as repo_adexchange
from models.ssp import ApplyAd

adexchange_router = APIRouter(
    prefix="/adexchange",
    tags = ['AdExchange']
)



@adexchange_router.post('/negotiate')
async def negotiate(request : Ad_Request):
    return repo_adexchange.negotiate(request)


@adexchange_router.post('/negotiate_interactive')
async def negotiate_interactive(request : Ad_Request):
    return repo_adexchange.negotiate_interactive(request)


@adexchange_router.post('/request')
async def request(request : ApplyAd):
    return repo_adexchange.request(request)

