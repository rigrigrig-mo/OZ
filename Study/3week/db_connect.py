# db_connect.py

from sqlalchemy import create_engine

def create_db_engine(db_name):
    db_info = DATABASES[db_name]
    engine = create_engine(f'mysql+pymysql://{db_info["user"]}:{db_info["password"]}@{db_info["host"]}/{db_info["database"]}')
    return engine
