from fastapi import APIRouter


authentication_router = APIRouter(
    tags= ['Authentication']
)




@authentication_router.post('/login')
async def login(user):
    return "login"