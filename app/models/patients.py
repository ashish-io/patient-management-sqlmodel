from sqlmodel import SQLModel, Field
from pydantic import model_validator
from ..utilities.service import calculate_bmi, calculate_verdict
from enum import Enum

class Gender(str, Enum):
  MALE = "male"
  FEMALE = "female"
  

class PatientsBase(SQLModel):
  
  name: str = Field(index= True)
  city: str
  age: int
  gender: Gender 
  height: float
  weight: float
  
  
class Patients(PatientsBase, table = True):
  id: int | None = Field(default= None, primary_key= True )
  bmi: float| None = Field(default= None)
  verdict: str| None = Field(default= None)

  
class PatientCreate(PatientsBase):
  pass 

class PatientView(PatientsBase):
  id: int
  
class PatientUpdate(SQLModel):
  
  name: str | None = None
  city: str | None = None
  age: int | None = None
  height: float | None = None
  weight: float | None = None
