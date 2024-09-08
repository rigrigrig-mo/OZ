from sqlalchemy import MetaData, create_engine, inspect


def main():
    print ("Hello world")

    engine = create_engine(f'mysql+pymysql://root:root@localhost:3306/oz')
    print (engine)

    metadata=MetaData()
    metadata.reflect(bind=engine)
    # print (metadata.tables)
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    print (tables)
    for table in tables:
        print (table)
        cols = inspector.get_columns(table)
        for col in cols:
            print(f"Column: {col['name']}, Type: {col['type']}")
    print("end")

   

    # print (inspector.get_view_names())
    # print (inspector.get_columns("invoices"))

if __name__ == "__main__":
    main()