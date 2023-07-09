import os
from sqlalchemy import create_engine # import function to create database engine
from sqlalchemy.orm.session import sessionmaker #import class to create a session handler to the database engine
from sqlalchemy.ext.declarative import declarative_base #import function

# Declare database name
database_name = "../database.sqlite"

# Get real path of this database.py file
base_dir = os.path.dirname(os.path.realpath(__file__))

# Get database location according to real path to this folder and the database_name
database_location = f"sqlite:///{os.path.join(base_dir, database_name)}"

# Create sqlalchemy engine to connect/create to the database location
engine = create_engine(database_location, echo=True)

# Create session handler to connect and bind to the database engine
Session = sessionmaker(bind=engine)

# Class to inherit from when creating database tables
Base = declarative_base()