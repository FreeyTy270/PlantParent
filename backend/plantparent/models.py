from datetime import date, timedelta
from typing import List

from pydantic import computed_field, field_validator
from typing_extensions import Annotated

from sqlmodel import SQLModel, Relationship, Field


class ItemBase(SQLModel):
    pass


class ApiResponse(SQLModel):
    success: Annotated[bool, Field(default=False, nullable=False)]
    message: Annotated[str, Field(default="")]
    error: Annotated[str | None, Field(default=None)]


class Room(ItemBase, table=True):
    name: Annotated[str | None, Field(default=None, primary_key=True)]
    plants: List["Plant"] | None = Relationship(back_populates="location")


class Plant(ItemBase, table=True):
    id: Annotated[int | None, Field(default=None, primary_key=True, unique=True, nullable=False)]
    nickname: Annotated[str, Field(unique=True, nullable=False)]
    plant_type: str
    scientific_name: Annotated[str | None, Field(default=None)]
    last_watered: date
    check_rate: int
    adoption_date: Annotated[date, Field(default=date.today(), nullable=False)]
    location_name: Annotated[
        str | None, Field(foreign_key="room.name", ondelete="SET NULL")
    ]
    location: Room | None = Relationship(
        sa_relationship_kwargs={"lazy": "joined"}, back_populates="plants")

    @field_validator("last_watered", "adoption_date", mode='before')
    @classmethod
    def check_date(cls, wannabe_date: date | str) -> date:
        print(f"Validator Received: {wannabe_date.__repr__()}")
        if not isinstance(wannabe_date, date):
            try:
                wannabe_date = wannabe_date.split('T')[0]
                print(f"Wannabe date after split: {wannabe_date}")
                wannabe_date = date.fromisoformat(wannabe_date)
            except ValueError:
                print(f"Invalid date format: {wannabe_date}")
                raise ValueError

        return wannabe_date

    @computed_field
    @property
    def next_check(self) -> date:
        if isinstance(self.last_watered, str):
            self.last_watered = date.fromisoformat(self.last_watered)

        return self.last_watered + timedelta(days=self.check_rate)

