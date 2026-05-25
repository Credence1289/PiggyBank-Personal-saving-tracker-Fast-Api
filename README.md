# PiggyBank API

<img width="747" height="494" alt="image" src="https://github.com/user-attachments/assets/619bdb7b-8a38-4939-8ad9-bde5d4a6c4b3" />


A modular personal savings tracker backend built using **FastAPI**.  
The project provides secure authentication, piggy bank management, transaction tracking, and clean REST API architecture using FastAPI and SQLAlchemy.

Designed as a backend portfolio project focused on scalable API structure, authentication systems, and financial transaction management.

---

# Features

- JWT Authentication & Authorization
- User Registration & Login
- Piggy Bank Creation & Management
- Deposit & Withdrawal Tracking
- Transaction History APIs
- RESTful API Design
- API Versioning using `/api/v1`
- Modular FastAPI Architecture
- SQLAlchemy ORM Integration
- Environment Variable Configuration
- Swagger/OpenAPI Documentation
- PostgreSQL

---

# Tech Stack

| Technology |     Purpose       |
|------------|-------------------|
| FastAPI    | Backend Framework |
| SQLAlchemy |      ORM          |
| Postgresql |    Database       |
| JWT        | Authentication    |
| Pydantic   | Data Validation   |
| Uvicorn    | ASGI Server       |
| Python     | Programming Language |

---

# Project Structure

```txt
PiggyBank/
│
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── api.py
│   │       └── routers/
│   │           ├── auth.py
│   │           ├── piggy.py
│   │           └── transactions.py
│   │
│   ├── core/
│   │   ├── gate.py
│   │   ├── security.py
│   │   └── token.py
│   │
│   ├── db/
│   │   ├── create_table.py
│   │   ├── dbengine.py
│   │   └── session.py
│   │
│   ├── models/
│   │   └── models.py
│   │
│   ├── schemas/
│   │   ├── piggybanks_schema.py
│   │   ├── transactions_schema.py
│   │   └── users_schema.py
│   │
│   └── main.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/Credence1289/PiggyBank-Personal-saving-tracker-Fast-Api.git
```

Move into the project directory:

```bash
cd PiggyBank
```

Create virtual environment:

```bash
python -m venv myenv
```

Activate virtual environment:

### Windows

```bash
myenv\Scripts\activate
```

### Linux/Mac

```bash
source myenv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Environment Setup

Create a `.env` file in the project root.

Example:

```env
DATABASE_URL=sqlite:///./piggybank.db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

# Run Locally

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Server runs on:

```txt
http://127.0.0.1:8000
```

---

# API Documentation

Swagger UI:

```txt
http://127.0.0.1:8000/docs
```

ReDoc:

```txt
http://127.0.0.1:8000/redoc
```

---

# Example API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/v1/register` | Register User |
| POST | `/api/v1/login` | Login User |
| POST | `/api/v1/piggy/create` | Create Piggy Bank |
| GET | `/api/v1/piggy/all` | Get User Piggy Banks |
| POST | `/api/v1/transactions/deposit` | Deposit Money |
| POST | `/api/v1/transactions/withdraw` | Withdraw Money |
| GET | `/api/v1/transactions/history` | Transaction History |

---

# Sample cURL Request

## Register User

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/register" \
-H "Content-Type: application/json" \
-d "{\"username\":\"vinayak\",\"email\":\"vinayak@example.com\",\"password\":\"password123\"}"
```

---

# Deployment

This project can be deployed on:

- Render
- Railway
- Docker
- VPS Servers

Example Render Start Command:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 10000
```

---

# Future Improvements

- Alembic Migrations
- Docker Support
- Async SQLAlchemy
- Redis Caching
- Pagination
- Monthly Analytics
- Budget Goals
- Email Verification
- Unit Testing
- CI/CD Pipelines

---

# GitHub Repository

https://github.com/Credence1289/PiggyBank-Personal-saving-tracker-Fast-Api

---

# Author

**Vinayak Dewoolkar**

Backend Developer focused on FastAPI, scalable API architecture, and backend engineering fundamentals.

---

# Project Goal

This project was built to strengthen backend development skills through authentication systems, database management, API architecture, and modular FastAPI development in a real-world style backend project.
