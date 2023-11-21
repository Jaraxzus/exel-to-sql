import datetime
from typing import Annotated

from sqlalchemy import Identity
from sqlalchemy.orm import (DeclarativeBase, Mapped, declared_attr,
                            mapped_column)

from sql.enums import DataTypes, QTypes

intpk = Annotated[int, mapped_column(primary_key=True)]


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"


class Table(Base):
    id: Mapped[intpk] = mapped_column(Identity())
    entry_id: Mapped[int]
    company: Mapped[str]
    data_type: Mapped[DataTypes]
    q_type: Mapped[QTypes]
    value: Mapped[int]
    date: Mapped[datetime.datetime]
