

# This file is for creating the database models
# functions must return dictionaries

# WARNING: DO NOT ERASE ANY CODE YOU HAVE NOT WRITE IN THIS FILES


# USER MODEL IS USED FOR USER REGISTRATION
def UserModel(email: str, hashedPassword: str) -> dict:
    User = {
        "email": email,
        "password": hashedPassword,
        # insert new fields above here
    }
    return User
