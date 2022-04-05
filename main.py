"""
Gunnar Bachmann Arcion Interview Project: Schema Compare

File: main.py

Authors: Gunnar Bachmann

Description: Compare tables within a given schema. Print table or column that differs in target from source
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

pg_conn = connect_to_db(user=PG_USER, password=PG_PASS, db=PG_DB, host=PG_HOST, port=PG_PORT)
pg_conn.close()
rs_conn = connect_to_db(user=RS_USER, password=RS_PASS, db=RS_DB, host=RS_HOST, port=RS_PORT)
rs_conn.close()
