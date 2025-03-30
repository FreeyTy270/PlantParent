
from sqlmodel import select, Session

from plantparent.models import Plant, Room

def test_adopt_a_plant(hire_scribe, buy_manufactured):
    new_plant = Plant(
        nickname="New Plant",
        scientific_name="Babyimus Plantus",
        check_rate=7,
        location=buy_manufactured,
    )

    hire_scribe.add_single(new_plant)

    with Session(hire_scribe.engine) as session:
        result = session.exec(select(Plant).join(Room)).first()

        plant = result
        plant_house = plant.location

    assert plant.nickname == "New Plant"
    assert plant_house.name == buy_manufactured.name


def test_plant_shopping_spree(hire_scribe, buy_manufactured):
    plants = ["Raven ZZ", "Neon Pothos", "Monstera", "Rubber Tree"]
    plants.sort()
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
            select(Plant)
            .join(Room)
            .where(Plant.nickname != "New Plant")
        )
        fetched_plants = sorted(result.fetchall(), key=lambda x: x.nickname)

    assert all(
        plant_name == plant.nickname for plant_name, plant in zip(plants, fetched_plants)
    )