# schema-compare
This Python program compares tables in a given schema between two databases. 

When the code (main.py) is executed, the program will go table by table between the source and target database to compare naming, data types, and ordering.
## How to run
1) Clone repository on your local machine.
2) Create the file config.py in the same directory as main.py
3) Copy the config.py template below and paste it into your config.py file.
4) Set the values in config.py
5) Run main.py
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
## Function Descriptions
- connect_to_db(user, password, db, host, port)
  - Establishes a connection to a database using credentials from config.py.
  - Returns database connection object.
- get_data(user, password, db, host, port)
  - Execute SQL statement to retrieve table information from the database and store the data in a pandas dataframe.
  - Returns a populated pandas dataframe.
- check_table(table, source_data, target_data)
  - Compare table structure between two databases and print where there is a mismatch.
  - Returns none.
- main()
  - Driving function for this program.
  - Returns none.
## Extra
- If you would like to use this program with a database other than Redshift or Postgres:
  -  You may need to adjust the SQL statement at the beginning of the main.py file (line 25).
  -  You might also have to change the column references in the main function (lines 107-117) along with the column references in the check_table function (lines 77-104).
