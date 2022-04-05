"""
Gunnar Bachmann Arcion Interview Project: Schema Compare

File: main.py

Authors: Gunnar Bachmann

Description: Compare tables within a given schema. Print table or column from source that is different in target.
"""

from config import *
import psycopg2


def connect_to_db(user, password, db, host, port):
    """
    Establish a connection to the database with username, password, and database name.
    Failed connection will result in a connection failed output to the user and program exit.

    :return: conn = connection to database
    """
    try:
        params = {
            'database': db,
            'user': user,
            'password': password,
            'host': host,
            'port': port
        }

        conn = psycopg2.connect(**params)
        print("Database connection established")
    except:
        print("Connection failed")
        exit()

    return conn

table_info_sql = """select table_name,
                           column_name,
                           ordinal_position,
                           data_type
                    from information_schema.columns
                    where table_schema = 'schema-check'
                    ORDER BY table_name ASC, ordinal_position ASC;"""

pg_conn = connect_to_db(user=PG_USER, password=PG_PASS, db=PG_DB, host=PG_HOST, port=PG_PORT)
pg_cur = pg_conn.cursor()
pg_cur.execute(table_info_sql)
pg_records = pg_cur.fetchall()
pg_cur.close()
pg_conn.close()
pg_dict = []
for record in pg_records:
    pg_dict.append(dict(zip(['table', 'columns', 'position', 'date_type'], record)))
print(pg_dict)




rs_conn = connect_to_db(user=RS_USER, password=RS_PASS, db=RS_DB, host=RS_HOST, port=RS_PORT)
rs_cur = rs_conn.cursor()
rs_cur.execute(table_info_sql)
rs_records = rs_cur.fetchall()
rs_cur.close()
rs_conn.close()
rs_dict = []
for record in rs_records:
    rs_dict.append(dict(zip(['table', 'columns', 'position', 'date_type'], record)))
print(rs_dict)
