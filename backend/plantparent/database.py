from sqlmodel import SQLModel, Session

from plantparent.models import ItemBase


class RecordsKeeper:
    def __init__(self, engine):
        self.engine = engine

    def add_single(self, item: ItemBase):
        with Session(self.engine) as session:
            session.add(item)
            session.commit()
            session.refresh(item)

    def add_multi(self, items: list[ItemBase]):
        with Session(self.engine) as session:
            for item in items:
                session.add(item)

            session.commit()

    def remove(self, item: ItemBase):
        with Session(self.engine) as session:
            session.delete(item)
            session.commit()
