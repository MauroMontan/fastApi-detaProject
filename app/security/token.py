from jose import JWTError, jwt
#from datetime import datetime, timedelta
from ..schemas.schemas import TokenData
from ..database.database import database


#! all commented code is for giving expire time to the token 

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
#ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    to_encode = data.copy()
    #expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    #to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verifyToken(token, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        user = database["USERS"].fetch({"email": email})._items

        email = user[0]["email"]
      

        if email is None:
            raise credentials_exception

        return TokenData(email=email)
    except JWTError:
        raise credentials_exception
