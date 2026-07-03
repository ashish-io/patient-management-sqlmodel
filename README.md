# Hospital Management API

A production-ready RESTful API for managing patients, doctors, and appointments, built with FastAPI and SQLModel.

## Live API
🚀 **https://web-production-cff72.up.railway.app/docs**

## Features

- Patient CRUD with automatic BMI calculation
- Doctor management
- Appointment booking system
- JWT Authentication with protected routes
- PostgreSQL database
- Dockerized for easy deployment
- Automated tests with Pytest
- CI/CD via Railway (auto deploys on git push)

## Tech Stack

- **FastAPI** — REST API framework
- **SQLModel** — ORM for database management
- **PostgreSQL** — Production database
- **JWT** — Authentication
- **Docker** — Containerization
- **Railway** — Cloud deployment
- **Pytest** — Testing

## Getting Started

### Option 1 — Run with Docker (Recommended)

Clone the repository:

```bash
git clone https://github.com/ashish-io/patient-management-sqlmodel.git
cd patient-management-sqlmodel
```

Create `.env` file:

```env
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
```

Run:

```bash
docker-compose up
```

API available at: 
http://localhost:8000/docs

### Option 2 — Run Locally

Clone and setup:

```bash
git clone https://github.com/ashish-io/patient-management-sqlmodel.git
cd patient-management-sqlmodel
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create `.env` file:

```env
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
```

Run:

```bash
uvicorn app.main:app --reload
```

## API Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/register` | Register a new user | No |
| POST | `/login` | Login and get JWT token | No |
| GET | `/patients` | Get all patients | Yes |
| POST | `/create` | Create a patient | Yes |
| GET | `/doctors` | Get all doctors | Yes |
| POST | `/add_doctor` | Add a doctor | Yes |
| POST | `/create_appointment` | Book appointment | Yes |

## Running Tests

```bash
pytest -v
```

## Project Structure

hospital_api/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models/
│   ├── routers/
│   └── utils/
├── Dockerfile
├── docker-compose.yml
├── .env.example
└── requirements.txt


## Author

GitHub: **[@ashish-io](https://github.com/ashish-io)**