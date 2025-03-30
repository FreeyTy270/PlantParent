from sqlmodel import SQLModel, Session, select

from plantparent.models import Home, Plant
from plantparent.database import RecordsKeeper


def test_build_a_home(hire_scribe):
    house = Home(name="Test House")

    hire_scribe.add_single(house)

    with Session(hire_scribe.engine) as session:
        result = session.exec(select(Home)).one()

    assert result.name == "Test House"

def test_demolition_team(hire_scribe, buy_manufactured):

    hire_scribe.remove(buy_manufactured)

    with Session(hire_scribe.engine) as session:
        result = session.exec(
            select(Home).where(Home.name == buy_manufactured.name)).one_or_none()

    assert not result


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


def test_plant_shopping_spree(hire_scribe, buy_manufactured):
    plants = ["Raven ZZ", "Neon Pothos", "Monstera", "Rubber Tree"]
    plant_objs = []

    for plant in plants:
        plant_objs.append(Plant(
            nickname=plant,
            check_rate=7,
            location=buy_manufactured,
        ))

    hire_scribe.add_multi(plant_objs)

    with Session(hire_scribe.engine) as session:
        result = session.exec(
            select(Plant).where(Plant.location_name == buy_manufactured.name)
            .order_by(Plant.nickname))

        result = [plant for plant in result]
    print(result)

    assert all(plant_name == plant.nickname for plant_name, plant in zip(plants,
                                                                     result))


