
from fastapi import APIRouter, status
from models.users import Advertiser, User
test_router = APIRouter(
    prefix="/test",
    tags = ['Test']
)


@test_router.post('/')
async def test(user : User):
    ad  = Advertiser.__init__(user)
    return ad