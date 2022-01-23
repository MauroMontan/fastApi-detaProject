from fastapi import FastAPI
from ..router import login, users


# ? from routes package you need to import the file that contains all your REST methods
# ? then just add your file in the routes list

#! do not erase login and users routes

routes = [
    login,
    users
]


#! do not modify this function

def initRoutes(app: FastAPI):
    for route in routes:
        app.include_router(route.router)
