from sqlmodel import SQLModel, Field
from typing import Annotated

class DoctorBase(SQLModel):
  name: str
  contact_no: str
  specialization: str
  experience: int 

class Doctor(DoctorBase, table = True):
  id: Annotated[int, Field(default = None, primary_key = True)]

class DoctorCreate(DoctorBase):
  pass

class DoctorView(DoctorBase):
  id: int

class DoctorUpdate(SQLModel):
  contact_no: str | None = None
  specialization: str | None = None
  experience: int | None = None