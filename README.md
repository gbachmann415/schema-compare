# schema-compare
## Description
This code compares tables in a given schema between two databases. When the code (main.py) is executed, the program
will go table by table between the source and target database to compare naming, data types, and ordering.
## General Information
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