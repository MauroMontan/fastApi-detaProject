from fastapi import FastAPI
from app.config.routes import initRoutes
from app.config.cors import initCors

# this project is created by @MauroMontan
#! Deta micros does not support static files


app = FastAPI(debug=True, title="App title")
initCors(app)
initRoutes(app)
