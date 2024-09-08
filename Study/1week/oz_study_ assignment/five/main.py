from sqlalchemy import MetaData
from conf.alchemy_db import engine


def getMetaData():
    metadata = MetaData()
    metadata.reflect(bind=engine)
    return metadata

def main():
    metadata = getMetaData()
    table_list = []
    for table_name, table in metadata.tables.items():
        table_list.append(table_name)
    print("Table List",table_list)
    print("Table Count: ", len(table_list))

if __name__ == "__main__":
    main()
