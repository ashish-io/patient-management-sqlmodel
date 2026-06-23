from fastapi import APIRouter, HTTPException
from typing import List
from sqlmodel import Session, select
from ..models.patients import PatientCreate, Patients, PatientUpdate, PatientView
from ..utilities.services import calculate_bmi, calculate_verdict
from ..database import engine

router = APIRouter()


@router.get("/patients",response_model=List[PatientView])   #change this , apply query parameters
def view_patients():
  with Session(engine) as session:
    patient = session.exec(select(Patients)).all()
    return patient


@router.get("/patients/{id}", response_model=PatientView)
def get_one_patient(id: int):
  with Session(engine) as session:
    statement = select(Patients).where(Patients.id == id )
    patient = session.exec(statement).first()

    if not patient:
      raise HTTPException(status_code= 404, detail="Patient not found")

    return patient

@router.post("/create")
def post_patient(patients: PatientCreate):
  with Session(engine) as session:
      data = patients.model_dump()

      patient = Patients.model_validate(data)

      session.add(patient)
      session.commit()
      session.refresh(patient)
      
      return patient

@router.patch("/edit/{id}", response_model= PatientView)
def edit_patient(id: int, patient: PatientUpdate):
  with Session(engine) as session:
    existing_patient = session.exec(select(Patients).where(Patients.id == id)).first()

    if not existing_patient:
      raise HTTPException(status_code=404, detail="Patient do not exist")
    
    patient_data = patient.model_dump(exclude_unset= True)
        
    updated_patient = existing_patient.sqlmodel_update(patient_data)

    updated_patient.bmi = calculate_bmi(updated_patient.height, updated_patient.weight)
    updated_patient.verdict = calculate_verdict(updated_patient.bmi)

    session.add(updated_patient)
    session.commit()

    session.refresh(updated_patient)
    return updated_patient


@router.delete("/delete/{id}")
def delete_patient(id: str):
  with Session(engine) as session:
    existing_patient = session.exec(select(Patients).where(Patients.id == id)).first()


    if not existing_patient:
      raise HTTPException(status_code=404, detail="Patient do not exist")
    
    session.delete(existing_patient)
    session.commit()
    return{"Deleted"}