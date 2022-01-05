

from pydantic import BaseModel


# this must have the same attributes that you have on your user model

class userSchema(BaseModel):
    email: str
    password: str
    # insert new fields above here

# dont erase this schema is,this is for verifying token,
# if you dont know about oauth2, dont add more attributes


class TokenData(BaseModel):
    email: str
