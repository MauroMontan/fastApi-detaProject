from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def initCors(app: FastAPI):
   # Here goes allowed connections
    origins = ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
