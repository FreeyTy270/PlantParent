from sqlmodel import SQLModel, create_engine, Session

from .models import Home, Plant


class RecordsKeeper:
    def __init__(self, db_path: str, debug: bool = False):
        self.engine = create_engine(db_path, echo=debug)

    def build_a_home(self, address: str) -> Home:
        new_home = Home(name=address)

        with Session(self.engine) as contractor:
            contractor.add(new_home)
            contractor.commit()
            contractor.refresh(new_home)

        return new_home

    def adopt_a_plant(
            self,
            name: str,
            check_rate: int,
    ) -> Plant:
        pass
