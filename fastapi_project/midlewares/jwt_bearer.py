# Third party imports
from fastapi.security import HTTPBearer
from fastapi.requests import Request
from fastapi import HTTPException

# Custom imports
import env_manager as em
import os
from jwt_manager import validate_token

em.load_env_cred()
ADMIN_CRED = {"username": os.getenv("AD_USER"), "passwd": os.getenv("AD_PASSWD")}

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        user_data = validate_token(auth.credentials)
        if user_data != ADMIN_CRED: 
            raise HTTPException(status_code=403, detail="Invalid Credentials!")