# Patient Management API

A REST API for managing patients, doctors, and appointments. Built with FastAPI and SQLModel.

## Features

- Patient CRUD with automatic BMI calculation
- Doctor management
- Appointment booking
- User registration and login with JWT

## Tech Stack

- FastAPI
- SQLModel
- SQLite
- JWT Authentication

## Run Locally

```bash
git clone https://github.com/ashish-io/patient-management-sqlmodel.git
cd patient-management-sqlmodel
python -m venv venv

# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate

pip install -r requirement.txt

# Create .env file with:
# SECRET_KEY=your-secret-key

uvicorn app.main:app --reload

## API Endpints

| Method | Endpoint              | Description      |
| ------ | --------------------- | ---------------- |
| POST   | `/register`           | Register user    |
| POST   | `/login`              | Login            |
| GET    | `/patients`           | List patients    |
| POST   | `/create`             | Create patient   |
| GET    | `/doctors`            | List doctors     |
| POST   | `/add_doctor`         | Add doctor       |
| POST   | `/create_appointment` | Book appointment |


##API Docs
After running, open: http://127.0.0.1:8000/docs


##Future Improvements
#Add tests
#Switch to PostgreSQL
#Add Docker support

##Author
GitHub: @ashish-io