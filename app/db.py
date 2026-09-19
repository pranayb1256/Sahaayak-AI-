from pathlib import Path
from sqlmodel import SQLModel,create_engine,Session
from typing import Generator



BASE_DIR = Path(__file__).resolve().parent
sqlite_url = f"sqlite:///{BASE_DIR}/database.db"
engine=create_engine(sqlite_url,echo=False,connect_args={"check_same_thread":False})

def create_db_and_tables()->None:
    SQLModel.metadata.create_all(engine)

def get_session()->Generator[Session,None,None]:
    with Session(engine) as session:
        yield session