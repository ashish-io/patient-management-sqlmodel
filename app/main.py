from fastapi import FastAPI
from .routers import patient, users

app = FastAPI()

app.include_router(patient.router)
app.include_router(users.router)



