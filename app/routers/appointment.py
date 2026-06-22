from fastapi import APIRouter, HTTPException
from ..models.appointment import Appointment, AppointmentView, AppointmentCreate, AppointmentUpdate
from sqlmodel import Session, select
from ..database import engine
from ..models.patients import Patients
from ..models.doctors import Doctor


router = APIRouter()


@router.post("/create_appointment", response_model = AppointmentView)
def create_appointment(appointment: AppointmentCreate):

  
  with Session(engine) as session:
    
    existing_doctor = session.exec(select(Doctor).where(appointment.doctors_id == Doctor.id)).all()
    if not existing_doctor:
      raise HTTPException(status_code = 404, detail = "Doctor not found")
    
    existing_patient = session.exec(select(Patients).where(appointment.patient_id == Patients.id)).all()
    if not existing_patient:
      raise HTTPException(status_code = 404, detail="Patient not found")
    

    new_appointment = Appointment.model_validate(AppointmentCreate)
    session.add(new_appointment)
    session.commit
    session.refresh(new_appointment)

    return new_appointment
  
@router.get("/see_patient_appointment/{p_id}")
def see_patient_appointment(p_id: str):
  with Session(engine) as session:
    patient_appointment = session.exec(select(Patients.p_id, Appointment).join(Appointment, Patients.id == Appointment.patient_id)).all()

    session.add(patient_appointment)
    session.commit()
    session.refresh(patient_appointment)

    return patient_appointment
  
@router.get("/get_doctor_appointment/{name}")
def see_doctor_appointment(name: str):
  with Session(engine) as session:
     

    d_id = session.exec(select(Doctor.id).where(Doctor.name == name))
    doctor_appointment = session.exec(select(Doctor.name, Appointment).join(Appointment, d_id == Appointment.doctors_id)).all()

    

    session.add(doctor_appointment)
    session.commit()
    session.refresh(doctor_appointment)

    return doctor_appointment


@router.patch("/update_appointment/{app_id}")
def update_appointment(app_id: int, new_appointment: AppointmentUpdate):

  new_info = new_appointment.model_dump(exclude_unset= True)

  with Session(engine) as session:

    appointment = session.get(Appointment, app_id)
    updated_appointment = appointment.sqlmodel_update(new_info)

    session.add(updated_appointment)
    session.commit()
    session.refresh(updated_appointment)

    return updated_appointment

  

  


    





