from sqlmodel import Session, select

from plantparent.models import Home, Plant


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
            select(Home).where(Home.name == buy_manufactured.name)
        ).one_or_none()

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
        result = session.exec(select(Plant).join(Home)).first()

        print(result)
        plant = result
        plant_house = plant.location
        print(plant_house)

    assert plant.nickname == "New Plant"
    assert plant_house.name == buy_manufactured.name


def test_plant_shopping_spree(hire_scribe, buy_manufactured):
    plants = ["Raven ZZ", "Neon Pothos", "Monstera", "Rubber Tree"]
    plant_objs = []

    for plant in plants:
        plant_objs.append(
            Plant(
                nickname=plant,
                check_rate=7,
                location=buy_manufactured,
            )
        )

    hire_scribe.add_multi(plant_objs)

    with Session(hire_scribe.engine) as session:
        result = session.exec(
            select(Plant, Home)
            .where(Plant.name != "Test Plant")
            .join(Home)
            .order_by(Plant.nickname)
        )
        print(result)
        result = [plant for plant in result]
        print(result)

    assert all(
        plant_name == plant.nickname for plant_name, plant in zip(plants.sort(), result)
    )
