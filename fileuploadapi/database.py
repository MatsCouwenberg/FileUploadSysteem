import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session as SQLAlchemySession

DATABASE_USER = os.getenv("POSTGRES_USER")
DATABASE_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DATABASE_HOST = os.getenv("POSTGRES_HOST")
DATABASE_NAME = os.getenv("POSTGRES_DB")

# PostgreSQL-URL for SQLAlchemy
SQLALCHEMY_DATABASE_URL = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:5432/{DATABASE_NAME}"
#SQLALCHEMY_DATABASE_URL = "mysql://root:1234@127.0.0.1:3306/datacentertest"


# Create an engine object to connect to the database
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a SessionLocal object to create sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Alias the SessionLocal as Session
Session = SessionLocal

# Create a Base object for declarative model definitions
Base = declarative_base()