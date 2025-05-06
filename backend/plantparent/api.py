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
    plant1 = Plant(nickname="Plant 1", scientific_name="Babymus Plantimus",
                   check_rate=7)
    plant2 = Plant(nickname="Plant 2", check_rate=14)
    plant3 = Plant(nickname="Plant 3", check_rate=21)

    current_plants = [
        plant1.model_dump(),
        plant2.model_dump(),
        plant3.model_dump(),
    ]
    return current_plants


if __name__ == "__main__":
    import sys
    import uvicorn

    uvicorn.run("plantparent.api:app", host="0.0.0.0", port=8000, reload=True)
    sys.exit(0)
