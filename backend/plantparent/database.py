from __future__ import annotations
from typing import TYPE_CHECKING

from sqlmodel import Session

if TYPE_CHECKING:
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
            session.add_all(items)
            session.commit()
            for item in items:
                session.refresh(item)

    def remove(self, item: ItemBase):
        with Session(self.engine) as session:
            session.delete(item)
            session.commit()

    def remove_multi(self, items: list[ItemBase]):
        with Session(self.engine) as session:
            for item in items:
                session.delete(item)

            session.commit()