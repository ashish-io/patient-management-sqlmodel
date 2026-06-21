from pwdlib import PasswordHash
import os
from dotenv import load_dotenv
import jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from sqlmodel import Session, select
from fastapi.security import OAuth2PasswordBearer
from ..models.users import User
from ..database import engine

token_extractor = OAuth2PasswordBearer(tokenUrl="/login")

load_dotenv()
SECRET_KEY = os.getenv("Secret_Key") or os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise RuntimeError("Missing SECRET_KEY environment variable")
ALGORITHM = "HS256"
TOKEN_EXPIRY_TIME = 30


password_hash = PasswordHash.recommended()



def create_hashed_password(plain_password: str):
  return password_hash.hash(plain_password)

def verify_password(plain_password, hashed_password): 
  return password_hash.verify(plain_password, hashed_password)

def create_token(username: str):
  payload = {
    "sub": username,
    "exp": datetime.utcnow() + timedelta(minutes = TOKEN_EXPIRY_TIME)
  }

  token = jwt.encode(payload, SECRET_KEY, ALGORITHM)
  return token



def verify_token(token: str = Depends(token_extractor)):
  try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    username = payload.get("sub")

    if username is None:
      raise HTTPException(status_code=401, detail="Invalid Token")
  except jwt.ExpiredSignatureError:
    raise HTTPException(status_code=401, detail="Token expired")
  except jwt.InvalidTokenError:
    raise HTTPException(status_code=401, detail="Invalid Token")
  
  with Session(engine) as session:
    user = session.exec(select(User).where(User.username == username)).first()
    if not user:
      raise HTTPException(status_code=401, detail="User not found")

  return user
