from sqlmodel import SQLModel,Field
from pydantic import model_validator
from utils import calculate_bmi, calculate_verdict


class PatientsBase(SQLModel):
  p_id: str
  name: str = Field(index= True)
  city: str
  age: int
  gender: str #chamge this later,,,use gender enum
  height: float
  weight: float
  bmi: float| None = Field(default= None)
  verdict: str| None = Field(default= None)

  @model_validator(mode = "after")
  def compute_field(self):
    if self.bmi is None:
      self.bmi = calculate_bmi(self.height, self.weight)
      

    if self.verdict is None:
      self.verdict = calculate_verdict(self.bmi)
    return self
  
class Patients(PatientsBase, table = True):
  id: int | None = Field(default= None, primary_key= True )
  
class PatientCreate(PatientsBase):
  pass 

class PatientView(PatientsBase):
  id: int
  
class PatientUpdate(SQLModel):
  p_id: str | None = None
  name: str | None = None
  city: str | None = None
  age: int | None = None
  height: float | None = None
  weight: float | None = None



class BaseUser(SQLModel):
  username: str
  email: str
  

class User(BaseUser, table = True):
  id: int | None = Field(default = None, primary_key = True)
  hashed_password: str

class UserView(BaseUser):
  pass

class UserCreate(BaseUser):
  password: str


