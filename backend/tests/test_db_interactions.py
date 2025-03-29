from sqlmodel import SQLModel, Session, select

from plantparent.models import Home, Plant
from plantparent.database import RecordsKeeper


def test_build_a_home(hire_scribe):
    house = Home(name="Test House")

    with Session(hire_scribe.engine) as session:
        session.add(house)
        session.commit()
        session.refresh(house)

        result = session.exec(select(Home)).one()

    assert result.name == "Test House"


def test_adopt_a_plant(hire_scribe, buy_manufactured):
    new_plant = Plant(
        nickname="New Plant",
        scientific_name="Babyimus Plantus",
        check_rate=7,
        location=buy_manufactured,
    )

    hire_scribe.add_single(new_plant)

    with Session(hire_scribe.engine) as session:
        result = session.exec(select(Plant)).one()

    print(result)
    assert result
