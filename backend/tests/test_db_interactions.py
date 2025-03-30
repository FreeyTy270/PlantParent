from sqlmodel import Session, select

from plantparent.models import Room, Plant


def test_build_a_home(hire_scribe):
    house = Room(name="Test House")

    hire_scribe.add_single(house)

    with Session(hire_scribe.engine) as session:
        result = session.exec(select(Room)).one()

    assert result.name == "Test House"


def test_demolition_team(hire_scribe, buy_manufactured):

    hire_scribe.remove(buy_manufactured)

    with Session(hire_scribe.engine) as session:
        result = session.exec(
            select(Room).where(Room.name == buy_manufactured.name)
        ).one_or_none()

    assert not result



