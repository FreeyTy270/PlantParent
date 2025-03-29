import json

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
    return {"Current Plants": ["Plant 1", "Plant 2", "Plant 3"]}
