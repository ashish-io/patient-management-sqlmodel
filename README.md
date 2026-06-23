# Patient Management API

A RESTful API for managing patients, doctors, and appointments, built with FastAPI and SQLModel.

## Features

- Patient CRUD operations
- Automatic BMI calculation for patients
- Doctor management
- Appointment booking system
- User registration and authentication with JWT
- SQLite database integration

## Tech Stack

- FastAPI
- SQLModel
- SQLite
- JWT Authentication
- Python

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/ashish-io/patient-management-sqlmodel.git
cd patient-management-sqlmodel
```

### Create and Activate a Virtual Environment

```bash
python -m venv venv
```

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key
```

### Run the Application

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/register` | Register a new user |
| POST | `/login` | Authenticate a user |
| GET | `/patients` | Retrieve all patients |
| POST | `/create` | Create a new patient |
| GET | `/doctors` | Retrieve all doctors |
| POST | `/add_doctor` | Add a new doctor |
| POST | `/create_appointment` | Book an appointment |

## API Documentation

Once the server is running, access the interactive Swagger UI at:

```text
http://127.0.0.1:8000/docs
```

## Future Improvements

- Add automated tests
- Migrate from SQLite to PostgreSQL
- Add Docker support
- Implement role-based access control (RBAC)
- Add pagination and filtering for API endpoints

## Author

GitHub: **@ashish-io**