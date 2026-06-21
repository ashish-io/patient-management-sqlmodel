from sqlmodel import SQLModel, Field

class BaseUser(SQLModel):
  username: str
  email: str
  

class User(BaseUser, table = True):
  id: int | None = Field(default = None, primary_key = True)
  hashed_password: str

class UserView(BaseUser):
  pass

class UserCreate(BaseUser):
  password: str