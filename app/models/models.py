# user model
def UserModel(email: str, hashedPassword: str) -> dict:
    User = {
        "email": email,
        "password": hashedPassword,
        #insert new fields above here
    }
    return User
