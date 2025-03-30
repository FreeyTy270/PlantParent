from datetime import date, timedelta
from typing import List

from pydantic import computed_field
from typing_extensions import Annotated

from sqlmodel import SQLModel, Relationship, Field


class ItemBase(SQLModel):
    pass


class Room(ItemBase, table=True):
    name: Annotated[str | None, Field(default=None, primary_key=True)]
    plants: List["Plant"] | None = Relationship(back_populates="location")


class Plant(ItemBase, table=True):
    id: Annotated[int | None, Field(default=None, primary_key=True)]
    nickname: str
    scientific_name: Annotated[str | None, Field(default=None)]
    last_watered: Annotated[date | None, Field(default=None)]
    check_rate: int
    adoption_date: Annotated[date, Field(default=date.today(), nullable=False)]
    location_name: Annotated[
        str | None, Field(foreign_key="room.name", ondelete="SET NULL")
    ]
    location: Room | None = Relationship(
        sa_relationship_kwargs={"lazy": "joined"}, back_populates="plants")

    @computed_field
    @property
    def next_check(self) -> date:
        return self.adoption_date + timedelta(self.check_rate)
