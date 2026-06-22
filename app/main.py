from fastapi import FastAPI
from .routers import patient, users, doctor, appointment
from contextlib import asynccontextmanager
from .database import create_db_and_table


@asynccontextmanager
async def lifespan(app: FastAPI):
  create_db_and_table()
  yield

app = FastAPI(lifespan = lifespan)

app.include_router(patient.router)
app.include_router(users.router)
app.include_router(doctor.router)
app.include_router(appointment.router)



