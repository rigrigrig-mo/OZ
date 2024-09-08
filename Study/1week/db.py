import json
import yaml
import random
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker

# 데이터베이스 연결 설정
DATABASE_URI = 'mysql+pymysql://root:0000@localhost/dbname'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()
metadata = MetaData(bind=engine)

# 설정 파일 읽기
def load_config(file_path):
    with open(file_path, 'r') as file:
        if file_path.endswith('.json'):
            return json.load(file)
        elif file_path.endswith('.yaml'):
            return yaml.safe_load(file)
        else:
            raise ValueError("Unsupported file format")

config = load_config('config.yaml')  

# 더미 데이터 생성 함수
def generate_dummy_data(table_name, num_records):
    table = Table(table_name, metadata, autoload_with=engine)
    dummy_data = []
    for _ in range(num_records):
        record = {column.name: random_value(column) for column in table.columns}
        dummy_data.append(record)
    return dummy_data

def random_value(column):
    if column.type.python_type == int:
        return random.randint(1, 100)
    elif column.type.python_type == str:
        return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10))
    # 필요한 경우 다른 데이터 타입도 추가
    return None

# 데이터베이스 초기화 또는 추가
for table_name, num_records in config['tables'].items():
    if config['reset_data']:
        session.execute(f'TRUNCATE TABLE {table_name}')
    dummy_data = generate_dummy_data(table_name, num_records)
    session.execute(Table(table_name, metadata).insert(), dummy_data)

session.commit()
session.close()
