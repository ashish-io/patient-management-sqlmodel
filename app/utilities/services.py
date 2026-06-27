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
