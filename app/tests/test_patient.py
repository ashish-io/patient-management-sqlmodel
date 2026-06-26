from ..models.patients import Patients, PatientCreate
from sqlmodel import Session
from ..utilities.services import calculate_bmi, calculate_verdict

def test_post_patient(client):

  data = {"name":"ashish", "city":"ktm", "age": 22, "gender":"male", "height": 1.2, "weight": 50}

  response = client.post("/create", json=data)
  
  assert response.status_code == 201
  assert response.json()["name"] == "ashish"
  assert response.json()["id"] is not None

def test_get_patient_by_name(client, test_session: Session):

  data = {"name":"ashish", "city":"ktm", "age": 22, "gender":"male", "height": 1.2, "weight": 50}

  patient1 = PatientCreate(**data)
  patient = Patients(**patient1.model_dump())
  test_session.add(patient)
  test_session.commit()
  test_session.refresh(patient)

  response = client.get(f"/patients/{patient.id}")
  
  response.status_code == 200

  response.json()["name"] == "ashish"
  response.json()["city"] == "ktm"
  response.json()["age"] == 22
  response.json()["bmi"] == calculate_bmi(response.json()["height"], response.json()["weight"])
  response.json()["verdict"] == calculate_verdict(response.json()["bmi"])
  response.json()["id"] is not None


def test_get_patients_by_query(client, test_session: Session):
  data = {"name":"ashish", "city":"ktm", "age": 22, "gender":"male", "height": 1.2, "weight": 50}

  patient1 = PatientCreate(**data)
  patient = Patients(**patient1.model_dump())
  test_session.add(patient)
  test_session.commit()
  test_session.refresh(patient)

  data = {"name":"Anish", "city":"ktm", "age": 22, "gender":"male", "height": 1.2, "weight": 50}

  patient1 = PatientCreate(**data)
  patient = Patients(**patient1.model_dump())
  test_session.add(patient)
  test_session.commit()
  test_session.refresh(patient)

  response = client.get("/patients",
    params = {"name": "Anish"}              
                        
    )
  response.status_code == 200
  response.json()[0]["name"] == "Anish"

  







