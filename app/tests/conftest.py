import pytest
from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.pool import StaticPool
from ..main import app
from ..database import get_session
from fastapi.testclient import TestClient
from ..utilities.authentication import verify_token

@pytest.fixture(scope = "function")
def test_session():
  TEST_DATABASE_URL = "sqlite://"

  engine = create_engine (
    TEST_DATABASE_URL,
    connect_args = {"check_same_thread":False},
    poolclass = StaticPool

  )

  SQLModel.metadata.create_all(engine)
  
  with Session(engine) as session:
    yield session

  SQLModel.metadata.drop_all(engine)

@pytest.fixture(scope = "function")
def client(test_session):

  def override_get_session():
    yield test_session
  
  app.dependency_overrides[get_session] = override_get_session

  yield TestClient(app)

  app.dependency_overrides.clear()

@pytest.fixture
def authenticated_client(client):
    fake_user = "hehe"
    app.dependency_overrides[verify_token] = lambda: fake_user
    yield client
    app.dependency_overrides.clear()
