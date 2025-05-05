import sys

import uvicorn
from sqlmodel import create_engine, SQLModel

from backend.plantparent.database import RecordsKeeper


def main():

    result: bool = True

    ## Setup db engine and make tables if needed
    sql_file = "sqlite:///plantparent.db"
    engine = create_engine(sql_file, echo=True)
    printing_press = RecordsKeeper(engine)
    SQLModel.metadata.create_all(engine)

    return True


if __name__ == "__main__":
    if main():
        uvicorn.run("plantparent.api:app", host="0.0.0.0", port=8000, reload=True)
        sys.exit(0)
    else:
        sys.exit(1)
