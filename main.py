from fastapi import FastAPI,HTTPException
from database import engine, create_db_and_table
from model import Patients, PatientView, PatientCreate, PatientUpdate
from utils import calculate_bmi, calculate_verdict,json_into_database
from sqlmodel import Session, select
from typing import List

app = FastAPI()

@app.get("/")
def home():
  return "An api to manage patients"


@app.get("/patients",response_model=List[PatientView])   #change this , apply query parameters
def view_patients():
  with Session(engine) as session:
    patient = session.exec(select(Patients)).all()
    return patient


@app.get("/patients/{p_id}", response_model=PatientView)
def get_one_patient(p_id: str):
  with Session(engine) as session:
    statement = select(Patients).where(Patients.p_id == p_id )
    patient = session.exec(statement).first()

    if not patient:
      raise HTTPException(status_code= 404, detail="Patient not found")

    return patient

@app.post("/create")
def post_patient(patients: PatientCreate):
  with Session(engine) as session:

    patient = Patients.model_validate(patients) #why this ? learn

    session.add(patient)
    session.commit()
    session.refresh(patient)
    return patient

@app.patch("/edit/{p_id}", response_model= PatientView)
def edit_patient(p_id: str, patient: PatientUpdate):
  with Session(engine) as session:
    existing_patient = session.exec(select(Patients).where(Patients.p_id == p_id)).first()

    if not existing_patient:
      raise HTTPException(status_code=404, detail="Patient do not exist")
    
    patient_data = patient.model_dump(exclude_unset= True)
        
    updated_patient = existing_patient.sqlmodel_update(patient_data)

    #update bmi, and verdict manually
    updated_patient.bmi = calculate_bmi(updated_patient.height, updated_patient.weight)
    updated_patient.verdict = calculate_verdict(updated_patient.bmi)
    session.add(updated_patient)

    session.commit()

    session.refresh(updated_patient)
    return updated_patient



@app.delete("/delete/{p_id}")
def delete_patient(p_id: str):
  with Session(engine) as session:
    existing_patient = session.exec(select(Patients).where(Patients.p_id == p_id)).first()

   

    if not existing_patient:
      raise HTTPException(status_code=404, detail="Patient do not exist")
    
    session.delete(existing_patient)
    session.commit()
    return{"Deleted"}


def main():
  pass
  #create_db_and_table()
  #json_into_database()   
    
if __name__ == "__main__":
  main()



