from enum import Enum



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
