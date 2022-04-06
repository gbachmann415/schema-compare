# schema-compare
This Python program compares tables in a given schema between two databases. 

When the code (main.py) is executed, the program will go table by table between the source and target database to compare naming, data types, and ordering.
## How to run
1) Create the file config.py in the same directory as main.py
2) Copy the config.py template below and paste it into your config.py file.
3) Set the values in config.py
4) Run main.py
## General Information
- Tested databases:
  - Postgres
  - Redshift
- Files:
  - main.py
  - config.py
  - .gitignore
  - README.md
- Credentials are stored in config.py
- config.py should be located in the same directory as main.py
- config.py template (PG prefix refers to the source database and RS prefix refers to the target database):
````
PG_USER = ""
PG_PASS = ""
PG_HOST = ""
PG_DB = ""
PG_PORT = 

RS_USER = ""
RS_PASS = ""
RS_HOST = ""
RS_DB = ""
RS_PORT = 

SCHEMA = ""
````
## Extra
- If you would like to use this program with a database other than Redshift or Postgres:
  -  You may need to adjust the SQL statement at the beginning of the main.py file (line 25).
  -  You might also have to change the column references in the main function (lines 107-117) along with the column references in the check_table function (lines 77-104).
