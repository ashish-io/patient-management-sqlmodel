from fastapi import APIRouter, HTTPException
from ..models.doctors import Doctor, DoctorView, DoctorCreate, DoctorUpdate
from sqlmodel import Session, select
from ..database import engine
from typing import List

router = APIRouter()

@router.post("/add_doctor", response_model = DoctorView)
def add_new_doctor(doctor: DoctorCreate):
  with Session(engine) as session:
   
  
   existing_doctor = session.exec(select(Doctor)).where(Doctor.name == doctor.name).where(Doctor.contact_no == doctor.contact_no).first()

   if existing_doctor:
     raise HTTPException(status_code = 201, detail = "Alreayd exist")
   
   new_doctor = Doctor(
     name = doctor.name,
     contact_no = doctor.contact_no,
     specialization = doctor.specialization,
     experience = doctor.experience
   )
   session.add(new_doctor)
   session.commit()
   session.refresh(new_doctor)
   
   return new_doctor

@router.get("/doctors", response_model = List[DoctorView])
def view_doctors():
  with Session(engine) as session:
    doctors = session.exec(select(Doctor)).all()
    return doctors

@router.get("/doctors/{name}", response_model = DoctorView)
def view_one_doctors(name: str):
  with Session(engine) as session:
    doctor = session.exec(select(Doctor).where(Doctor.name == name)).first()
    return doctor
  
@router.patch("/edit_doctor/{name}", response_model = DoctorView)
def edit_doctor_detail(name: str, doctor: DoctorUpdate):
  with Session(engine) as session:
    existing_doctor = session.exec(select(Doctor).where(Doctor.name == name)).first()

    if not existing_doctor:
      raise HTTPException(status_code = 201, detail = "Do not exist")
    
    new_data = doctor.model_dump(exclude_unset = True)
    updated_data = existing_doctor.sqlmodel_update(new_data)

    session.add(updated_data)
    session.commit()
    session.refresh(updated_data)

    return updated_data

@router.delete("/delete_doctors/{name}")
def delete_doctors(name: str):
  with Session(engine) as session:
    existing_doctor = session.exec(select(Doctor).where(Doctor.name == name)).first()

    if not existing_doctor:
      raise HTTPException(status_code = 201, detail = "Do not exist")

  session.delete(existing_doctor)
  session.commit()

  return {"message": "Deleted"}  
    


