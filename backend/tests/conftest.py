from pathlib import Path

import pytest
from sqlalchemy.exc import IntegrityError
from sqlmodel import SQLModel, Session, create_engine

from plantparent import models
from plantparent.database import RecordsKeeper


@pytest.fixture(scope="session")
def reset_db():
    cwd = Path(__file__).parent
    test_db = Path(cwd, "test.db")
    if test_db.exists():
        test_db.unlink()


@pytest.fixture(scope="session")
def create_db_engine(reset_db):
    sql_path = "sqlite:///backend/tests/test.db"
    test_engine = create_engine(sql_path)
    SQLModel.metadata.create_all(test_engine)

    yield test_engine


@pytest.fixture(scope="session")
def hire_scribe(create_db_engine):
    yield RecordsKeeper(create_db_engine)


@pytest.fixture
def buy_manufactured(hire_scribe):
    home_address = 1
    house = models.Home(name="Manufactured Home")
    try:
        hire_scribe.add_single(house)
    except IntegrityError:
        house.name = f"Manufactured Home {home_address}"
        hire_scribe.add_single(house)
        home_address += 1

    return house
