from sqlmodel import create_engine, SQLModel, Session

sqlite_filename = "Database.db"
sqlite_url = f"sqlite:///{sqlite_filename}"
engine = create_engine(sqlite_url)

def create_db_and_table():
  SQLModel.metadata.create_all(engine)

def get_session():
  with Session(engine) as session:
    yield session

