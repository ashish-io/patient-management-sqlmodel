from sqlmodel import SQLModel, Field
from pydantic import model_validator
from enum import Enum


class Roles(str, Enum):
  ADMIN = "admin"
  USER = "user"


class User(SQLModel, table = True):
  username: str
  email: str
  id: int | None = Field(default = None, primary_key = True)
  hashed_password: str
  role: Roles = Field(default="user")

class UserView(SQLModel):
  username: str
  email: str

class UserCreate(SQLModel):
  username: str
  email: str
  password: str
  confirm_password: str

  @model_validator(mode = "after")
  def check_password(self):
    if self.password != self.confirm_password:
      raise ValueError("Password Do not match")
    return self





