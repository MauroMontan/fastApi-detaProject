from fastapi import APIRouter
from fastapi.params import Depends
from ..database.database import database
from ..security.hashing import Hash
from ..models.models import UserModel
from ..schemas.schemas import userSchema
from ..security.oauth2 import getCurrentUser

router = APIRouter(prefix="/users", tags=["users"])

#this method creates new users in deta base
@router.post("/signup")
async def insert(request: userSchema):
    hashedPassword = Hash.bcrypt(request.password)
    user = database["USERS"].insert(
        UserModel(request.email, hashedPassword))
    return user

#this method list all users in deta base
@router.get("/user-list")
async def getUsers(currentUser: userSchema = Depends(getCurrentUser)):
    users = database["USERS"].fetch()._items
    return users