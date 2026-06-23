from sqlmodel import SQLModel, Field
from pydantic import  field_validator, computed_field
from ..utilities.services import calculate_bmi, calculate_verdict
from enum import Enum

class Gender(str, Enum):
  MALE = "male"
  FEMALE = "female"
    
 
class Patients(SQLModel, table = True):
  id: int | None = Field(default= None, primary_key= True )
  name: str
  city: str
  age: int
  gender: Gender
  height: float
  weight: float
  bmi: float| None = Field(default= None)
  verdict: str| None = Field(default= None)

  
class PatientCreate(SQLModel):
  name: str
  city: str
  age: int
  gender: Gender
  height: float
  weight: float

  @field_validator("age")
  @classmethod
  def check_age(cls, v):
    if v < 0:
      raise ValueError("Age cannot be negative")
    return v
  
  @field_validator("height")
  @classmethod
  def check_height(cls,v):
    if v < 0.5 or v > 2.5:
      raise ValueError("Height must be between 0.5meter to 2.5 meter")
    return v
  
  @field_validator("weight")
  @classmethod
  def check_weight(cls, v):
    if v < 1 or v > 500:
      raise ValueError("Weight must be between 1 kg t0 500kg")
    return v
  

  @computed_field
  def calculate_bmi(self) -> float| None:
    bmi = calculate_bmi(self.height, self.weight)
    return bmi
  
  @computed_field
  def calculate_verdict(self) -> str:
    verdict = calculate_verdict(self.bmi)
    return verdict


class PatientView(SQLModel):
  id: int
  name: str 
  city: str
  age: int
  gender: Gender 
  height: float
  weight: float
  
 
class PatientUpdate(SQLModel):
  
  name: str | None = None
  city: str | None = None
  age: int | None = None
  height: float | None = None
  weight: float | None = None

  @computed_field
  def calculate_bmi(self) -> float| None:
    bmi = calculate_bmi(self.height, self.weight)
    return bmi
  
  @computed_field
  def calculate_verdict(self) -> str:
    verdict = calculate_verdict(self.bmi)
    return verdict
    



