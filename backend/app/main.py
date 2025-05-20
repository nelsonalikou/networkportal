# app/main.py
from fastapi import FastAPI
from app.database import Base, engine
from app.routers import users, ports
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import json

app = FastAPI()

Base.metadata.create_all(bind=engine)


load_dotenv()

allow_origins = json.loads(os.getenv("ALLOW_ORIGINS"))

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,  # replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # allows POST, GET, OPTIONS, etc.
    allow_headers=["*"],  # allows Authorization, Content-Type, etc.
)

app.include_router(users.router)
app.include_router(ports.router)

@app.get("/")
async def root():
    return {"message": "Bienvenue sur Network Portal !"}
