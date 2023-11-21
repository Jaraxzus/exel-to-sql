import datetime

from pydantic import BaseModel

from sql.models import DataTypes, QTypes


class TableBase(BaseModel):
    entry_id: int
    company: str
    data_type: DataTypes
    q_type: QTypes
    value: int
    date: datetime.datetime
