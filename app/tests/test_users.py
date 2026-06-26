from sqlmodel import Session
from ..models.users import User
from ..utilities.authentication import create_hashed_password

def test_login(client, test_session: Session):
  user = User(
    username = "Ashish",
    email = "ashish@gmail.com",
    hashed_password = create_hashed_password("password")
  )

  test_session.add(user)
  test_session.commit()
  test_session.refresh(user)

  response = client.post("/login", data={"username": "Ashish", "password": "password"})
  assert response.status_code == 200
  assert "access_token" in response.json()

def test_login_with_wrongpassword(client, test_session):
  user = User(
    username = "Ashish",
    email = "ashish@gmail.com",
    hashed_password = create_hashed_password("password")
  )

  test_session.add(user)
  test_session.commit()
  test_session.refresh(user)

  response = client.post("/login", data={"username": "Ashish", "password": "wrongpassword"})
  assert response.status_code == 401
  assert response.json()["detail"] == "Wrong Password"

def test_login_user_donot_exist(client, test_session):

  respose = client.post("/login", data = {"username": "anythin", "password": "pass"})
  assert respose.status_code == 404
  assert respose.json()["detail"] == "User Not Found"


#test for protected route

def test_protected_user(authenticated_client):

  response = authenticated_client.get("/user")
  response.status_code == 200
  response.json() == "hello"

def test_protected_user_with_no_token(client):

  response = client.get("/user")
  assert response.status_code == 401

def test_protected_user_with_invalid_token(client):

  response = client.get("/user", headers = {"Authorization": "Bearer randomtoken"})
  assert response.status_code == 401




  