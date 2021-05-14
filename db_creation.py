import sqlite3
import parser

class Connection():
    db = 'car_base.db'
    __count = 0
    __instance = None

    def __new__(cls, *args, **kwargs):  # Singleton
        if not isinstance(cls.__instance, cls):
            cls.__instance = super(Connection, cls).__new__(cls)

    def __init__(self, db):
        self.__db = db

    def new_table(name_table,data):
        column_names = data[0]
        conn = sqlite3.connect(Connection.db)
        cur = conn.cursor()
        query = 'CREATE TABLE IF NOT EXISTS ' + name_table + '('
        for key, value in column_names.items():
            query += key
            if type(value) == int:
                query += ' INT,'
            elif type(value) == float:
                query += ' FLOAT,'
            else:
                query += ' TEXT,'
        query = query[:-1]
        query += ');'
        cur.execute(query)
        cur.close()
        conn.close()
    def insert_db(table,data):
        columns = data[0].keys()
        data_modified = []
        for item in data:
            data_modified.append(tuple(item.values()))
        col_names_str = ''
        symbol_num = ''
        for col_name in columns:
            col_names_str += f'{col_name},'
            symbol_num += ',?'
        conn =sqlite3.connect(Connection.db)
        cur = conn.cursor()
        query = 'INSERT OR REPLACE INTO ' + table + ' ( ' + col_names_str[:-1] + ' ) VALUES (?' + symbol_num[:-2] + ');'
        cur.executemany(query, data_modified)
        conn.commit()
        cur.close()
        conn.close()

data_base = Connection
#data_base.new_table('car',parser.cars)
#data_base.insert_db('car',parser.cars)
#data_base.new_table('diller',parser.dillers_info)
#data_base.insert_db('diller',parser.dillers_info)