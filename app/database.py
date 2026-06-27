from sqlmodel import create_engine, SQLModel, Session
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")



# sqlite_filename = "Database.db"
# sqlite_url = f"sqlite:///{sqlite_filename}"
engine = create_engine(DATABASE_URL)

def create_db_and_table():
  SQLModel.metadata.create_all(engine)

def get_session():
  with Session(engine) as session:
    yield session

