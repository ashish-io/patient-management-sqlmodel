from sqlmodel import SQLModel, Field
from datetime import datetime, date, time
from typing import Annotated
from enum import Enum

class Status(str,Enum):
  PENDING = "pending"
  COMPLETED = "completed"


class Appointment(SQLModel, table = True):
  appointment_id: int | None = Field(default = None, primary_key = True)
  patient_id: int | None = Field(default = None, foreign_key = "patients.id")
  doctors_id: int | None = Field(default = None, foreign_key = "doctor.id")
  status: Status = Field(default = "pending")
  appointment_date: date
  appointment_time: time
  booking_date: Annotated[datetime, Field(default_factory = datetime.utcnow)]

class AppointmentCreate(SQLModel):
  patient_id: int | None = Field(default = None, foreign_key = "patients.id")
  doctors_id: int | None = Field(default = None, foreign_key = "doctor.id")
  appointment_date: date
  appointment_time: time


class AppointmentView(SQLModel):
  patient_id: int | None = Field(default = None, foreign_key = "patients.id")
  doctors_id: int | None = Field(default = None, foreign_key = "doctor.id")
  status: Status
  appointment_date: date
  appointment_time: time

class AppointmentUpdate(SQLModel):
  status: Status | None = None
  

