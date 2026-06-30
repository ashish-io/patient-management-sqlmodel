from .authentication import verify_token
from fastapi import Depends,HTTPException 
from typing import Annotated
from ..models.users import User

def calculate_bmi(height, weight):
  return round(weight/(height**2),2)



def calculate_verdict(bmi):
  if bmi < 18.5:
      verdict = "Underweight"
  elif bmi < 25:
     verdict = "Normal"
  elif bmi < 30:
      verdict = "Overweight"
  else:
      verdict = "Obese"
  return verdict

def verify_role(role: str):
   def get_role(current_user: User = Depends(verify_token)):
      if role != current_user.role:
         raise HTTPException(status_code=403, detail="unauthorized")
      return current_user
   return get_role
      

   
   
   

    

   

   