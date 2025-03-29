
from datetime import date
from typing import List

from pydantic import ConfigDict
from typing_extensions import Annotated

from sqlmodel import SQLModel, Relationship, Field, Date

class ItemBase(SQLModel):
    pass


class Home(ItemBase, table=True):
    name: Annotated[str | None, Field(default=None, primary_key=True)]
    plants: List["Plant"] | None = Relationship(back_populates="location")


class Plant(ItemBase, table=True):
    id: Annotated[int | None, Field(default=None, primary_key=True)]
    last_watered: Annotated[date | None, Field(default=None, nullable=False)]
    check_rate: int
    adoption_date: Annotated[date, Field(default=date.today(), nullable=False)]
    location_name: Annotated[str, Field(foreign_key="home.name")]
    location: Home | None = Relationship(back_populates="plants")

