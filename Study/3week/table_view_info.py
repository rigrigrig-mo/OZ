# table_view_info.py

from sqlalchemy import MetaData, inspect
from db_connect import create_db_engine

def get_table_info(db_name, schema):
    engine = create_db_engine(db_name)
    metadata = MetaData()
    metadata.reflect(bind=engine, only=[schema])
    inspector = inspect(engine)
    table_info = []
    for table_name in metadata.tables.keys():
        table_columns = []
        for column in metadata.tables[table_name].columns:
            column_info = {
                'name': column.name,
                'type': column.type.compile(engine),
                'nullable': column.nullable,
                'comment': inspector.get_column_comment(table_name, column.name)
            }
            table_columns.append(column_info)
        table_info.append({
            'name': table_name,
            'columns': table_columns,
            'comment': inspector.get_table_comment(table_name)
        })
    return table_info
