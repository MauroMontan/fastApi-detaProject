from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status
from ..database.database import db
from ..security.hashing import Hash
from ..security.token import create_access_token


router = APIRouter(prefix="/login", tags=["login"])


#! DO NOT ERASE ANY CODE YOU HAVE NOT WRITE

@router.post("/")
async def login(request: OAuth2PasswordRequestForm = Depends()):

    user = db.table("USERS").fetch({"email": request.username})._items

    try:
        password = user[0]["password"]
        email = user[0]["email"]
    except:
        password = str()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="user not found")

    if not Hash.verify(password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="incorrect password")

    if user:
        access_token = create_access_token(
            data={"sub": email}
        )
        return {"user": user[0], "access_token": access_token, "token_type": "bearer"}
