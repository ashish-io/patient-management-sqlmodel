from sqlmodel import SQLModel, Field
from datetime import datetime, date, time
from typing import Annotated
from enum import Enum

class Status(str,Enum):
  PENDING = "pending"
  COMPLETED = "completed"

class AppointmentBase(SQLModel): 
  patient_id: int | None = Field(default = None, foreign_key = "patients.id")
  doctors_id: int | None = Field(default = None, foreign_key = "doctor.id")
  status: Status
  appointment_date: date
  appointment_time: time
  

class Appointment(AppointmentBase, table = True):
   appointment_id: int | None = Field(default = None, primary_key = True)
   booking_date: Annotated[datetime, Field(default_factory = datetime.utcnow)]

class AppointmentCreate(AppointmentBase):
  pass 

class AppointmentView(AppointmentBase):
  pass

class AppointmentUpdate(AppointmentBase):
  status: Status | None = None
  

