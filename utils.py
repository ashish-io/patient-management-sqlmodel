from sqlmodel import Session
import json
from model import Patients
from database import engine

def calculate_bmi(height, weight) -> float:
  bmi = round(weight / (height ** 2), 2)
  return bmi

def calculate_verdict(bmi) -> str:
  if bmi < 18.5:
      verdict = "Underweight"
  elif bmi < 25:
     verdict = "Normal"
  elif bmi < 30:
      verdict = "Overweight"
  else:
      verdict = "Obese"
  return verdict


def json_into_database():

  with open("patients.json", "r") as f:
    data = json.load(f)

  with Session(engine) as session:

    for key, value in data.items():

      patient = Patients(p_id = key,**value)
      session.add(patient)
    session.commit()