from exel_parser.parser import read_exel
from sql.models import Table
from sql.querys.orm import SyncORM
from sql.schemas import TableBase


def pydantic_model_to_alchemy(table: TableBase) -> Table:
    table_dict = table.model_dump()
    return Table(**table_dict)


def migrate_exel_to_sql() -> None:
    path = "table.xlsx"
    pydantic_objects = read_exel(path)
    if pydantic_objects:
        objects = []
        for i in pydantic_objects:
            objects.append(pydantic_model_to_alchemy(i))
        SyncORM.table_insert(objects)


def main() -> None:
    migrate_exel_to_sql()
    SyncORM.get_total()


if __name__ == "__main__":
    main()
