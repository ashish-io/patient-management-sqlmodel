from pwdlib import PasswordHash
import os
from dotenv import load_dotenv
import jwt
from datetime import datetime, timedelta


load_dotenv()
SECRET_KEY = os.getenv("Secret_Key")
ALGORITHM = "HS256"
TOKEN_EXPIRY_TIME  = 30



password_hash = PasswordHash.recommended()

def create_hashed_password(plain_password: str):
  return password_hash.hash(plain_password)

def verify_password(plain_password, hashed_password): 
  return password_hash.verify(plain_password, hashed_password)

def create_token(username: str):

  payload = {
    "username": username,
    "exp": datetime.utcnow() + timedelta(minutes = TOKEN_EXPIRY_TIME)
  }

  token = jwt.encode(payload, SECRET_KEY, ALGORITHM)

  return token

def verify_token(token: str):
  pass

