from sqlalchemy import func, select

from sql.database import SessionLocal
from sql.models import Table
from sql.schemas import TableBase


class SyncORM:
    @staticmethod
    def table_insert(objs: list[TableBase]):
        with SessionLocal() as session:
            session.add_all(objs)
            session.commit()

    @staticmethod
    def get_total():
        """SELECT date, q_type, SUM(value) AS total FROM tables GROUP BY date, q_type"""
        with SessionLocal() as session:
            query = select(Table.date, Table.q_type, func.sum(Table.value)).group_by(
                Table.date, Table.q_type
            )
            results = session.execute(query).all()
            for result in results:
                result = result.tuple()
                print(
                    f"Дата: {result[0].strftime('%Y-%m-%d')}, {result[1].value},  Тотал: {result[2]}"
                )
