from ..models.doctors import Doctor
from sqlmodel import Session

def test_post_doctors(client):
  data = {"name": "arati", "contact_no": "4343", "specialization": "eye", "experience":4}

  response = client.post("/add_doctor", json=data)


  assert response.status_code == 201
  
  assert response.json()["name"] == "arati"
  assert response.json()["contact_no"] == "4343"
  assert response.json()["specialization"] == "eye"
  assert response.json()["experience"] == 4
  

def test_post_same_doctors(client):
  data_1 = {
    "name": "arati",
    "contact_no": "4343",
    "specialization": "eye",
    "experience":4
    }
  
  response_1 = client.post("/add_doctor", json=data_1)

  body_1 = response_1.json()

  assert response_1.status_code == 201


  #again post data with same name 

  data_2= {
    "name": "arati",
    "contact_no": "4354343",
    "specialization": "brain",
    "experience":44
    }
  
  response_2 = client.post("/add_doctor", json=data_2)

  body_2 = response_2.json()

  assert response_2.status_code == 400
  assert body_2["detail"] == "Already exist"


def test_get_doctots(client, test_session: Session):
  
  doctor1 = Doctor(
    name = "Ashish",
    contact_no="322",
    specialization="eye",
    experience=4
  )

  doctor2 = Doctor(
    name = "keshab",
    contact_no="433",
    specialization="brain",
    experience=5
  )

  test_session.add(doctor1)
  test_session.add(doctor2)
  test_session.commit()

  response = client.get("/doctors")

  assert response.status_code == 200
  assert len(response.json()) == 2

def test_get_doctor_by_name(client, test_session: Session):

  doctor1 = Doctor(
    name = "Ashish",
    contact_no="322",
    specialization="eye",
    experience=4
  )
  
  test_session.add(doctor1)
  test_session.commit()
  test_session.refresh(doctor1)

  response = client.get(f"/doctors/{doctor1.name}")

  assert response.status_code == 200
  assert response.json()["name"] == "Ashish"
  
