from pathlib import Path

import pytest
from sqlmodel import SQLModel, Session, create_engine

from plantparent import models
from plantparent.database import RecordsKeeper


@pytest.fixture(scope="session")
def reset_db():
    test_db = Path("test.db")
    if test_db.exists():
        test_db.unlink()


@pytest.fixture(scope="session")
def create_db_engine(reset_db):
    sql_path = "sqlite:///test.db"
    test_engine = create_engine(sql_path)
    SQLModel.metadata.create_all(test_engine)

    yield test_engine


@pytest.fixture(scope="session")
def hire_scribe(create_db_engine):
    yield RecordsKeeper(create_db_engine)


@pytest.fixture
def buy_manufactured(hire_scribe):
    house = models.Home(name="Test House")

    with Session(hire_scribe.engine) as session:
        session.add(house)
        session.commit()
        session.refresh(house)

    return house
