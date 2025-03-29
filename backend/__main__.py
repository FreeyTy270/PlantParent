
from sqlmodel import create_engine, SQLModel

from backend.app.database import RecordsKeeper
from backend.app.models import Home, Plant


def main():
    sql_file = "sqlite:///plantparent.db"

    printing_press = create_engine(sql_file, echo=True)
    SQLModel.metadata.create_all(printing_press)
    scribe = RecordsKeeper(printing_press)

    house = Home(name="House")

    scribe.add_single(house)

    print(f"Finished adding {house.__str__()}")


if __name__ == "__main__":
    main()

