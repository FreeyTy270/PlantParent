import logging
from datetime import datetime

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from plantparent.models import Plant

app = FastAPI(debug=True, title="PlantParent", version="0.1.0")
log = logging.getLogger(__file__)

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
    print(f"Answering a response at {datetime.now()}!!")
    plant1 = Plant(
        nickname="Plant 1", scientific_name="Babymus Plantimus", check_rate=7
    )
    plant2 = Plant(nickname="Plant 2", check_rate=14)
    plant3 = Plant(nickname="Plant 3", check_rate=21)

    current_plants = [
        plant1.model_dump(),
        plant2.model_dump(),
        plant3.model_dump(),
    ]
    return current_plants

class PlantName(BaseModel):
    nickname: str
    
@app.post("/add")
async def add(plant_name: PlantName):
    message = ''
    error = None
    success = False
    try:
        print(f"Adding plant: {plant_name}")
        message = f"Added plant: {plant_name}"
        success = True
    except Exception as e:
        error = str(e)
        message = f"Error adding plant: {plant_name}"
    finally:
        return {
            "success": success,
            "message": message,
            "error": error,
                }



if __name__ == "__main__":
    import sys
    import uvicorn

    uvicorn.run("plantparent.api:app", host="0.0.0.0", port=8000, reload=True)
    sys.exit(0)
