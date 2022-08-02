from fastapi import APIRouter


authentication_router = APIRouter(
    prefix="/",
    tags= "Authentication"
)




@authentication_router.post('/login')
async def login(user):
    return "login"