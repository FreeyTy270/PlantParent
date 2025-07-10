import logging
from datetime import datetime, date, timedelta
from typing import Annotated

from pydantic import BaseModel
from sqlmodel import SQLModel, create_engine, Session, select
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from plantparent.database import RecordsKeeper
from plantparent.models import Plant, ApiResponse

app = FastAPI(debug=True, title="PlantParent", version="0.1.0")
sql_path = "sqlite:///backend/plantparent.db"
records_engine = create_engine(sql_path)
SQLModel.metadata.create_all(records_engine)
records = RecordsKeeper(records_engine)
log = logging.getLogger(__file__)

origins = [
        "http://localhost:5173",
        "http://192.168.50.85:5173",
]

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Svelte dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def date_validator(wannabe_date: str | date) -> date:
    if isinstance(wannabe_date, str):
        d_string = wannabe_date.split('T')[0]
        wannabe_date = date.fromisoformat(d_string)

    return wannabe_date

@app.get("/existing")
async def existing():
    print(f"Fetching all existing plants {datetime.now()}!!")
    with Session(records.engine) as session:
        current_plants = session.exec(select(Plant)).all()

    return current_plants

class PlantName(BaseModel):
    nickname: str
    
@app.post(path="/add", status_code=201)
async def add(new_plant: Plant):

    resp = ApiResponse()
    plant_name = new_plant.nickname
    new_plant.adoption_date = date_validator(new_plant.adoption_date)
    new_plant.last_watered = date_validator(new_plant.last_watered)

    try:
        print(f"Adding a plant: {plant_name}")
        with Session(records.engine) as session:
            session.add(new_plant)
            session.commit()
            session.refresh(new_plant)
        resp.message = f"Your application to adopt {plant_name} has been approved!"
        resp.success = True
    except Exception as e:
        resp.error = str(e)
        resp.message = f"Error adding new plant: {plant_name}"
    finally:
        return resp.model_dump(mode="json")

@app.delete("/bury")
async def delete(fallen_id: int):
    resp = ApiResponse()

    try:
        with Session(records.engine) as session:
            fallen_plant = session.exec(select(Plant).where(Plant.id ==
                                                            fallen_id)).first()
            fallen_name = fallen_plant.nickname
            session.delete(fallen_plant)
            session.commit()
            resp.success = True
            resp.message = f"{fallen_name} has been laid to rest"
    except Exception as e:
        resp.error = str(e)
        resp.message = f"Error removing plant: {fallen_name}"

    print(resp.message)

    return resp.model_dump(mode="json")


if __name__ == "__main__":
    import sys
    import uvicorn

    uvicorn.run("plantparent.api:app", host="0.0.0.0", port=8000, reload=True)
    sys.exit(0)
