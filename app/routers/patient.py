from fastapi import APIRouter, HTTPException, Query, Depends
from typing import List
from sqlmodel import Session, select
from ..models.patients import PatientCreate, Patients, PatientUpdate, PatientView
from ..utilities.services import calculate_bmi, calculate_verdict
from ..database import engine, get_session

router = APIRouter(tags=["Patient"])


@router.get("/patients",response_model=List[PatientView])   
def view_patients(
  name: str | None = Query(default = None, description = "Search by name"),
  city: str | None = Query(default = None, description = "Filter by city"),
  skip: int  = Query(default = 0, ge = 0, description = "Skip N patients"),
  limit: int = Query(default = 10, ge = 1, le = 50, description = "Maximum patients to return"),
  
  session: Session = Depends(get_session)
):
  

    statement = select(Patients)
    if name:
      statement = statement.where(Patients.name == name)
    if city:
      statement = statement.where(Patients.city == city)
    statement = statement.offset(skip).limit(limit)
    patient = session.exec(statement).all()
    return patient


@router.get("/patients/{id}", response_model=PatientView)
def get_one_patient(id: int, session: Session = Depends(get_session)):
  
    statement = select(Patients).where(Patients.id == id )
    patient = session.exec(statement).first()

    if not patient:
      raise HTTPException(status_code= 404, detail="Patient not found")

    return patient

@router.post("/create", status_code=201)
def post_patient(patients: PatientCreate, session: Session = Depends(get_session)):
  
      data = patients.model_dump()

      patient = Patients.model_validate(data)

      session.add(patient)
      session.commit()
      session.refresh(patient)
      
      return patient

@router.patch("/edit/{id}", response_model= PatientView)
def edit_patient(id: int, patient: PatientUpdate, session: Session = Depends(get_session)):
  
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
def delete_patient(id: int, session: Session = Depends(get_session)):
  
    existing_patient = session.exec(select(Patients).where(Patients.id == id)).first()


    if not existing_patient:
      raise HTTPException(status_code=404, detail="Patient do not exist")
    
    session.delete(existing_patient)
    session.commit()
    return{"Deleted"}