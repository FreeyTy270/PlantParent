from __future__ import annotations

from datetime import date
from typing_extensions import Annotated

from sqlmodel import SQLModel, Field, Date


class Home(SQLModel, table=True):
    name: Annotated[str | None, Field(default=None, primary_key=True)]
    plants: Annotated[list[Plant], Field(default_factory=list)]


class Plant(SQLModel, table=True):
    id: Annotated[int | None, Field(default=None, primary_key=True)]
    last_watered: Annotated[Date | None, Field(default=None, nullable=False)]
    check_rate: int
    location: Annotated[Home, Field(foreign_key="home.id")]
    adoption_date: Annotated[Date, Field(default=date.today(), nullable=False)]
