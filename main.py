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
import json
import pandas as pd
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
        # print("Database connection established")
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
    # Establish connection
    conn = connect_to_db(user=user, password=password, db=db, host=host, port=port)
    df = pd.read_sql(table_info_sql, conn)
    conn.close()
    return df


def check_table(table, source_data, target_data):
    if len(target_data) == 0:
        print("Table: " + table)
    else:

    return


def main():
    # Get source data
    pg_data = get_data(user=PG_USER, password=PG_PASS, db=PG_DB, host=PG_HOST, port=PG_PORT)
    # Get target data
    rs_data = get_data(user=RS_USER, password=RS_PASS, db=RS_DB, host=RS_HOST, port=RS_PORT)

    tables = pg_data.table_name.unique()
    for i in tables:
        check_table(i, pg_data[pg_data.table_name.isin([i])], rs_data[rs_data.table_name.isin([i])])




main()
