# ddl_script.py

from sqlalchemy import create_engine, text
from db_connect import create_db_engine

def generate_ddl_script(db_name, table_name):
    engine = create_db_engine(db_name)
    ddl_script = text(engine.dialect.ddl_compiler(engine.connect(), None).get_table_ddl(table_name))
    return ddl_script
