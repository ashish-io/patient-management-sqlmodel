from sqlmodel import SQLModel, Field
from typing import Annotated


class Doctor(SQLModel, table = True):
  id: Annotated[int, Field(default = None, primary_key = True)]
  name: str
  contact_no: str
  specialization: str
  experience: int


class DoctorCreate(SQLModel):
  name: str
  contact_no: str
  specialization: str
  experience: int

class DoctorView(SQLModel):
  
  name: str
  contact_no: str
  specialization: str
  experience: int

class DoctorUpdate(SQLModel):
  contact_no: str | None = None
  specialization: str | None = None
  experience: int | None = None