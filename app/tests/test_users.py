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
  respose.status_code == 404
  respose.json()["detail"] == "User Not Found"







  