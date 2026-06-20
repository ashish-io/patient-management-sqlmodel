
from model import UserCreate, User
from sqlmodel import Session, select
from database import engine
from fastapi import HTTPException, APIRouter, Depends
from authentication import create_hashed_password, verify_password, create_token
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

token_extractor = OAuth2PasswordBearer(tokenUrl = "login")

router = APIRouter()



@router.post("/register")
def register(user: UserCreate):
  with Session(engine) as session:
    #check if user already exist
    existing_user = session.exec(select(User).where(User.username == user.username).where(User.email == user.email)).first()

    if  existing_user:
      raise HTTPException(status_code= 201, detail = "User alreayd exist")
    
    new_user = User(
      username = user.username,
      email = user.email,
      hashed_password = create_hashed_password(user.password)

    )
    
    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return new_user
  
@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
  with Session(engine) as session:
    user = session.exec(select(User).where(form_data.username == User.username)).first() 

    if not user:
      raise HTTPException(status_code = 404, detail = "User Not Found")

    if not verify_password(form_data.password, user.hashed_password):
      raise HTTPException(status_code = 401, detail = "Wrong Password")
    
    token = create_token(form_data.username)

  return {"my_token": token, "token_type": "bearer"}

  

      



  pass






