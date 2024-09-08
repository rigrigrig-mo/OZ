# schema_table_info.py

# sqlalchemy 라이브러리를 이용하여 데이터베이스 엔진을 생성하는 함수를 가져옵니다.
from sqlalchemy import MetaData, inspect
from db_connect import create_db_engine

# 특정 데이터베이스의 스키마 목록을 반환하는 함수입니다.
def get_schemas(db_name):
    # create_db_engine 함수를 이용하여 데이터베이스 엔진을 생성합니다.
    engine = create_db_engine(db_name)
    # MetaData 클래스를 이용하여 메타데이터 객체를 생성합니다.
    metadata = MetaData()
    # reflect 메서드를 이용하여 데이터베이스 엔진에서 스키마 정보를 가져옵니다.
    metadata.reflect(bind=engine)
    # metadata.tables.keys()를 이용하여 스키마 목록을 반환합니다.
    return metadata.tables.keys()

# 특정 데이터베이스의 스키마에 속한 테이블 정보를 반환하는 함수입니다.
def get_table_info(db_name, schema):
    # create_db_engine 함수를 이용하여 데이터베이스 엔진을 생성합니다.
    engine = create_db_engine(db_name)
    # MetaData 클래스를 이용하여 메타데이터 객체를 생성합니다.
    metadata = MetaData()
    # reflect 메서드를 이용하여 데이터베이스 엔진에서 스키마 정보를 가져옵니다.
    metadata.reflect(bind=engine, only=[schema])
    # inspect 클래스를 이용하여 데이터베이스 엔진의Inspector 객체를 생성합니다.
    inspector = inspect(engine)
    # 테이블 정보를 저장할 리스트를 생성합니다.
    table_info = []
    # metadata.tables.keys()를 이용하여 스키마에 속한 테이블 목록을 가져옵니다.
    for table_name in metadata.tables.keys():
        # 테이블의 컬럼 정보를 저장할 리스트를 생성합니다.
        table_columns = []
        # metadata.tables[table_name].columns를 이용하여 테이블의 컬럼 목록을 가져옵니다.
        for column in metadata.tables[table_name].columns:
            # 컬럼 정보를 딕셔너리 형태로 저장합니다.
            column_info = {
                'name': column.name,
                'type': column.type.compile(engine),
                'nullable': column.nullable,
                'comment': inspector.get_column_comment(table_name, column.name)
            }
            # 컬럼 정보를 테이블 컬럼 리스트에 추가합니다.
            table_columns.append(column_info)
        # 테이블 정보를 딕셔너리 형태로 저장합니다.
        table_info.append({
            'name': table_name,
            'columns': table_columns,
            'comment': inspector.get_table_comment(table_name)
        })
    # 테이블 정보를 반환합니다.
    return table_info
