import json

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from plantparent.models import Plant

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Svelte dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Welcome to the Sensor Dashboard API"}


@app.get("/existing")
async def existing():
    print("Answering a response!!")
    current_plants = [
        Plant(nickname="Plant 1", check_rate=7),
        Plant(nickname="Plant 2", check_rate=14),
        Plant(nickname="Plant 3", check_rate=21),
    ]
    return {current_plants}
