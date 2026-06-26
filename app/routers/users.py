from fastapi import APIRouter, HTTPException, Depends
from ..models.users import UserCreate, UserView, User
from sqlmodel import Session, select
from ..database import engine, get_session
from fastapi.security import OAuth2PasswordRequestForm
from ..utilities.authentication import create_hashed_password, create_token, verify_password, verify_token

router = APIRouter(tags = ["Users"])


@router.post("/register")
def register(user: UserCreate, session: Session = Depends(get_session)):

    #check if user already exist
    existing_user = session.exec(select(User).where(User.username == user.username).where(User.email == user.email)).first()

    if  existing_user:
      raise HTTPException(status_code= 401, detail = "User alreayd exist")
    
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
def login(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
  
    user = session.exec(select(User).where(form_data.username == User.username)).first() 

    if not user:
      raise HTTPException(status_code = 404, detail = "User Not Found")

    if not verify_password(form_data.password, user.hashed_password):
      raise HTTPException(status_code = 401, detail = "Wrong Password")
    
    token = create_token(form_data.username)

    return {"access_token": token, "token_type": "bearer"}


#just a example protected endpoint
@router.get("/user", dependencies = [Depends(verify_token)])
def get_user():
  return "hello"
