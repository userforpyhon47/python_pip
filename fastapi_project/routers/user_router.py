# Third party imports
from fastapi import APIRouter
from fastapi.responses import JSONResponse

# Custom imports
import env_manager as em
from jwt_manager import create_token

# import database connection
from schemas.user_schema import User

# bult-in import
import os

# Create router app
user_router = APIRouter()

# Test user for authenticating with JWT
em.load_env_cred()
ADMIN_CRED = {"username": os.getenv("AD_USER"), "passwd": os.getenv("AD_PASSWD")}

#Endpoint for login and getting JWT auth token
@user_router.post("/login", tags=["Login"], response_model=str)
def login(user: User):
    if user.dict() == ADMIN_CRED:
        token = create_token(user.dict())
        return JSONResponse(status_code=200, content=token)
    return JSONResponse(status_code=401, content=[])


