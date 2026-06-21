from fastapi import APIRouter, HTTPException
from typing import List
from sqlmodel import Session, select
from ..models.patients import PatientCreate, Patients, PatientUpdate, PatientView
from ..utilities.service import calculate_bmi, calculate_verdict
from ..database import engine

router = APIRouter()


@router.get("/patients",response_model=List[PatientView])   #change this , apply query parameters
def view_patients():
  with Session(engine) as session:
    patient = session.exec(select(Patients)).all()
    return patient


@router.get("/patients/{p_id}", response_model=PatientView)
def get_one_patient(p_id: str):
  with Session(engine) as session:
    statement = select(Patients).where(Patients.p_id == p_id )
    patient = session.exec(statement).first()

    if not patient:
      raise HTTPException(status_code= 404, detail="Patient not found")

    return patient

@router.post("/create")
def post_patient(patients: PatientCreate):
  with Session(engine) as session:

    patient = Patients.model_validate(patients) #why this ? learn

    session.add(patient)
    session.commit()
    session.refresh(patient)
    return patient

@router.patch("/edit/{p_id}", response_model= PatientView)
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



@router.delete("/delete/{p_id}")
def delete_patient(p_id: str):
  with Session(engine) as session:
    existing_patient = session.exec(select(Patients).where(Patients.p_id == p_id)).first()

   

    if not existing_patient:
      raise HTTPException(status_code=404, detail="Patient do not exist")
    
    session.delete(existing_patient)
    session.commit()
    return{"Deleted"}