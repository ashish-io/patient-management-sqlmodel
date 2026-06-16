from sqlmodel import create_engine, SQLModel
from model import Patients

sqlite_filename = "patient_database.db"
sqlite_url = f"sqlite:///{sqlite_filename}"
engine = create_engine(sqlite_url)

def create_db_and_table():
  SQLModel.metadata.create_all(engine)

