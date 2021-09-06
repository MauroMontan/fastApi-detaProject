from fastapi import FastAPI
from app.config.routes import initRoutes
from app.config.cors import initCors

# this project is created by @MauroMontan

app = FastAPI(debug=True,title="Recipe API")
initCors(app)
initRoutes(app)