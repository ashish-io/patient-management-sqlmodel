def calculate_bmi(hieght, weight):
  return round(weight/(hieght**2),2)



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
