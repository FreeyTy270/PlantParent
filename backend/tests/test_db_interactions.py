from sqlmodel import Session, select

from plantparent.models import Room, Plant


def test_build_a_home(hire_scribe):

    living_room = Room(name="Living Room")
    bedroom = Room(name="Bedroom")
    dining_room = Room(name="Dining Room")
    green_room = Room(name="Green")

    house = [living_room, bedroom, dining_room, green_room]

    hire_scribe.add_multi(house)

    with Session(hire_scribe.engine) as session:
        result = session.exec(select(Room)).all()

    assert all([x.name == y.name for x, y in zip(house, result)])


def test_demolition_team(hire_scribe, buy_manufactured):

    hire_scribe.remove(buy_manufactured)

    with Session(hire_scribe.engine) as session:
        result = session.exec(
            select(Room).where(Room.name == buy_manufactured.name)
        ).one_or_none()

    assert not result



