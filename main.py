"""
Arcion Interview Project: Schema Compare

File: main.py

Authors: Gunnar Bachmann

Notes: Utilizes a config.py file created by user (should be in same directory as this file, main.py)

Description: Compare tables within a given schema.
             Print table or column from source that is different in target.
"""

from config import *
import psycopg2
#TODO add input from user. schema, db (source and target)

table_info_sql = """select table_name,
                           column_name,
                           ordinal_position,
                           data_type
                    from information_schema.columns
                    where table_schema = 'schema-check'
                    ORDER BY table_name ASC, ordinal_position ASC;"""


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


def get_data(user, password, db, host, port):
    """
    Gather data from given DB

    :param user: DB username
    :param password: DB password
    :param db: DB name
    :param host: DB host
    :param port: DB port
    :return: List containing result data
    """
    conn = connect_to_db(user=user, password=password, db=db, host=host, port=port)
    cur = conn.cursor()
    cur.execute(table_info_sql)
    records = cur.fetchall()
    cur.close()
    conn.close()
    result_list = []
    for record in records:
        result_list.append(dict(zip(['table', 'columns', 'position', 'date_type'], record)))
    return result_list


def main():
    pg_data = get_data(user=PG_USER, password=PG_PASS, db=PG_DB, host=PG_HOST, port=PG_PORT)
    rs_data = get_data(user=RS_USER, password=RS_PASS, db=RS_DB, host=RS_HOST, port=RS_PORT)


main()
