# main.py

from config import DATABASES
from schema_table_info import get_schemas, get_table_info
from ddl_script import generate_ddl_script
from excel_file import create_excel_file

def main():
    db_name = 'db1'  # 사용할 DB 접속 정보 이름
    schema = 'public'  # 조회할 스키마 이름

    # 스키마 목록 조회
    schemas = get_schemas(db_name)
    print(f'Schemas: {schemas}')

    # 테이블 정보 조회
    table_info = get_table_info(db_name, schema)
    print(f'Table Info: {table_info}')

    # 뷰 정보 조회
    # view_info = get_view_info(db_name, schema)
    # print(f'View Info: {view_info}')

    # 테이블 DDL 스크립트 생성
    table_name = 'users'  # 생성할 테이블 이름
    ddl_script = generate_ddl_script(db_name, table_name)
    print(f'DDL Script: {ddl_script}')

    # 엑셀 파일 생성
    table_info_excel = create_excel_file(table_info, 'table_info.xlsx')
    view_info_excel = create_excel_file(view_info, 'view_info.xlsx')

    print(f'Table Info Excel: {table_info_excel}')
    print(f'View Info Excel: {view_info_excel}')

if __name__ == "__main__":
    main()
