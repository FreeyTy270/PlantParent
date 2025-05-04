import sys

from sqlmodel import create_engine, SQLModel

from backend.plantparent.database import RecordsKeeper
from backend.plantparent.models import Room, Plant


def main():

    result: bool = True

    ## Setup db engine and make tables if needed
    sql_file = "sqlite:///plantparent.db"
    printing_press = create_engine(sql_file, echo=True)
    SQLModel.metadata.create_all(printing_press)

    ## Create db interaction object
    scribe = RecordsKeeper(printing_press)

    house = Room(name="House")

    scribe.add_single(house)

    print(f"Finished adding {house.__str__()}")

    return True


if __name__ == "__main__":
    if main():
        sys.exit(0)
    else:
        sys.exit(1)
