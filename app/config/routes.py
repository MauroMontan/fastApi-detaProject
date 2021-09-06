from ..router import login,users

# this is how a route is included app.include_router(ROUTERNAME.router)

def initRoutes(app):
     app.include_router(login.router)
     app.include_router(users.router)
  
