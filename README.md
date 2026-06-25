# PiggyBank API

<<img width="754" height="599" alt="endpoints" src="https://github.com/user-attachments/assets/dcceef5e-8d9b-4009-a76b-17c37d9b4d5f" />
>

A production-oriented personal savings tracker backend built with **FastAPI** and **PostgreSQL**. This project demonstrates modern backend development practices including JWT-based authentication, database migrations, containerization, and clean REST API architecture.

**[GitHub Repository](https://github.com/Credence1289/PiggyBank-Personal-saving-tracker-Fast-Api)**

---

## 🎯 Project Overview

PiggyBank API is a scalable backend service that manages user accounts, piggy bank accounts, and financial transactions. It serves as a real-world application demonstrating enterprise-grade API design patterns, secure authentication mechanisms, and database management practices.

This project was built to strengthen backend development expertise in:
- **Secure Authentication**: JWT tokens with access and refresh token patterns
- **Database Management**: Schema migrations using Alembic, ORM relationships with SQLAlchemy
- **Containerization**: Docker and Docker Compose for reproducible environments
- **API Design**: RESTful principles with API versioning and modular architecture
- **Code Organization**: Separation of concerns with dedicated layers for routing, business logic, and data access

---

## ✨ Features

- **Authentication & Authorization**
  - JWT-based authentication with access and refresh tokens
  - Secure password hashing and token validation
  - Protected endpoints with dependency injection

- **User Management**
  - User registration with email validation
  - Secure login with token generation
  - User profile management

- **Piggy Bank Management**
  - Create and manage multiple piggy banks per user
  - Track individual savings goals
  - Piggy bank metadata and status tracking

- **Transaction Tracking**
  - Deposit and withdrawal operations
  - Complete transaction history with timestamps
  - Transaction validation and balance reconciliation

- **API Design**
  - RESTful API with `/api/v1` versioning
  - Comprehensive Swagger/OpenAPI documentation
  - Request validation with Pydantic schemas
  - Consistent error handling and response formats

- **Infrastructure**
  - PostgreSQL with SQLAlchemy ORM
  - Database migrations with Alembic
  - Docker containerization with Docker Compose
  - Environment-based configuration with Pydantic Settings
  - ASGI server with Uvicorn

---

## 🏗️ Architecture Highlights

### Modular Design
The application follows a layered architecture pattern:
- **API Layer** (`/api/v1`): Route handlers and endpoint definitions
- **Business Logic**: Service layer with core functionality
- **Database Layer**: SQLAlchemy ORM models and session management
- **Security Layer**: JWT token management and password hashing
- **Schemas Layer**: Pydantic models for request/response validation

### Key Design Patterns
- **Dependency Injection**: FastAPI dependencies for authentication and database sessions
- **Token-Based Authentication**: Stateless auth using JWT with refresh token rotation
- **Database Migrations**: Schema versioning with Alembic for safe deployments
- **Configuration Management**: Environment variables via Pydantic Settings
- **Error Handling**: Standardized HTTP exception handling

---

## 📋 Tech Stack

| Technology | Purpose | Version |
|------------|---------|---------|
| **FastAPI** | Async web framework | 0.100+ |
| **SQLAlchemy** | ORM for database operations | 2.0+ |
| **PostgreSQL** | Relational database | 12+ |
| **Alembic** | Database schema migrations | 1.12+ |
| **Pydantic** | Data validation and settings | 2.0+ |
| **JWT (PyJWT)** | Token-based authentication | 2.8+ |
| **Uvicorn** | ASGI application server | 0.23+ |
| **Docker** | Container orchestration | 20.10+ |
| **Docker Compose** | Multi-container deployment | 2.20+ |
| **Python** | Programming language | 3.10+ |

---

## 📁 Project Structure

```
PiggyBank/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── api.py                 # API router aggregator
│   │       └── routers/
│   │           ├── auth.py            # Authentication endpoints
│   │           ├── piggy.py           # Piggy bank management
│   │           └── transactions.py    # Transaction operations
|   |           └── health_check.py    # health check
│   │
│   ├── core/
│   │   ├── config.py                  # Pydantic settings
│   │   ├── security.py                # Password hashing & JWT validation
│   │   └── token.py                   # Token generation & verification
│   │
│   ├── db/
│   │   ├── base.py                    # SQLAlchemy declarative base
│   │   ├── engine.py                  # Database engine initialization
│   │   └── session.py                 # Session management
│   │
│   ├── models/
│   │   └── models.py                  # SQLAlchemy ORM models
│   │
│   ├── schemas/
│   │   ├── base.py                    # Common schemas
│   │   ├── users_schema.py            # User request/response schemas
│   │   ├── piggy_schema.py            # Piggy bank schemas
│   │   └── transactions_schema.py     # Transaction schemas
│   │
│   └── main.py                        # FastAPI app initialization
│
├── alembic/
│   ├── versions/                      # Migration files
│   ├── env.py                         # Migration environment config
│   └── script.py.mako                 # Migration template
│
├── migrations/                        # Database migration runner (optional)
├── tests/                             # Unit and integration tests
│
├── .env.example                       # Environment variables template
├── .env.local                         # Local development env (git ignored)
├── .dockerignore                      # Docker build optimization
├── .gitignore                         # Git ignore rules
├── Dockerfile                         # Container image definition
├── docker-compose.yml                 # Multi-container setup
├── alembic.ini                        # Alembic configuration
├── requirements.txt                   # Python dependencies
└── README.md                          # This file
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- PostgreSQL 12+ (or use Docker)
- pip or uv package manager
- Docker & Docker Compose (optional)

### Option 1: Docker (Recommended)
```bash
# Clone repository
git clone https://github.com/Credence1289/PiggyBank-Personal-saving-tracker-Fast-Api.git
cd PiggyBank

# Start services with Docker Compose
docker-compose up --build

# Run migrations (in another terminal)
docker-compose exec api alembic upgrade head

# Access the API
# Swagger UI: http://localhost:8000/docs
# ReDoc: http://localhost:8000/redoc
```

### Option 2: Local Development
```bash
# Clone repository
git clone https://github.com/Credence1289/PiggyBank-Personal-saving-tracker-Fast-Api.git
cd PiggyBank

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your PostgreSQL credentials

# Run migrations
alembic upgrade head

# Start server
uvicorn app.main:app --reload

# Access the API at http://localhost:8000
```

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root (copy from `.env.example`):

```env
# Database Configuration
DATABASE_URL=postgresql://user:password@localhost:5432/piggybank
# Format: postgresql://username:password@host:port/database

# JWT Security
SECRET_KEY=your_super_secret_key_change_this_in_production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7

# Application
APP_NAME=PiggyBank API
APP_VERSION=1.0.0
DEBUG=True
```

### Environment Variable Reference

| Variable | Description | Example |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL connection string | `postgresql://user:pass@localhost:5432/piggybank` |
| `SECRET_KEY` | JWT signing key (keep secret!) | `your_secret_key_here` |
| `ALGORITHM` | JWT encoding algorithm | `HS256` |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Access token validity period | `30` |
| `REFRESH_TOKEN_EXPIRE_DAYS` | Refresh token validity period | `7` |
| `APP_NAME` | Application name for docs | `PiggyBank API` |
| `DEBUG` | Enable debug mode (disable in production) | `False` |

---

## 🐳 Docker Setup

### Using Docker Compose (Recommended)

```bash
# Start all services (API + PostgreSQL)
docker-compose up --build

# View logs
docker-compose logs -f api

# Stop services
docker-compose down

# Rebuild without cache
docker-compose up --build --no-cache
```

### Docker Compose Services
- **api**: FastAPI application on port 8000
- **db**: PostgreSQL database on port 5432

### Manual Docker Build
```bash
# Build image
docker build -t piggybank-api:latest .

# Run container
docker run -p 8000:8000 \
  --env-file .env \
  piggybank-api:latest

# With PostgreSQL (requires running DB)
docker run -p 8000:8000 \
  --env DATABASE_URL=postgresql://user:pass@host:5432/db \
  --env SECRET_KEY=your_key \
  piggybank-api:latest
```

---

## 📚 Development Workflow

### Initial Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env

# Configure your .env file with local database
nano .env  # Edit with your PostgreSQL credentials
```

### Database Migrations
```bash
# Create new migration
alembic revision --autogenerate -m "Add user table"

# Review migration file in alembic/versions/

# Apply migrations
alembic upgrade head

# Rollback last migration
alembic downgrade -1

# View migration history
alembic history
```

### Running the Application
```bash
# Development mode with auto-reload
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Production mode (without reload)
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Accessing Documentation
Once the server is running:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

### Docker Compose Workflow
```bash
# Start services
docker-compose up --build

# Run migrations inside container
docker-compose exec api alembic upgrade head

# View logs
docker-compose logs -f api

# Access Swagger UI
# Navigate to http://localhost:8000/docs

# Stop services
docker-compose down
```

---

## 📖 API Endpoints

### Authentication
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|----------------|
| POST | `/api/v1/auth/register` | Register new user | No |
| POST | `/api/v1/auth/login` | Login and get tokens | No |
| POST | `/api/v1/auth/refresh` | Refresh access token | Yes |

### Piggy Banks
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|----------------|
| POST | `/api/v1/piggy/create` | Create piggy bank | Yes |
| GET | `/api/v1/piggy/all` | List user's piggy banks | Yes |
| GET | `/api/v1/piggy/{id}` | Get piggy bank details | Yes |
| DELETE | `/api/v1/piggy/{id}` | Delete piggy bank | Yes |

### Transactions
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|----------------|
| POST | `/api/v1/transactions/deposit` | Deposit money | Yes |
| POST | `/api/v1/transactions/withdraw` | Withdraw money | Yes |
| GET | `/api/v1/transactions/history` | Transaction history | Yes |
| GET | `/api/v1/transactions/history/{piggy_id}` | Piggy bank transaction history | Yes |


###Health Check
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|----------------|
| GET | `/api/v1/health` | Health check | No |
---

## 🧪 Example Requests

### Register User
```bash
curl -X POST "http://localhost:8000/api/v1/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "secure_password_123"
  }'
```

### Login
```bash
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "password": "secure_password_123"
  }'
```

### Create Piggy Bank
```bash
curl -X POST "http://localhost:8000/api/v1/piggy/create" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer {access_token}" \
  -d '{
    "name": "Vacation Fund",
    "target_amount": 5000.00,
    "description": "Summer vacation savings"
  }'
```

### Deposit Money
```bash
curl -X POST "http://localhost:8000/api/v1/transactions/deposit" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer {access_token}" \
  -d '{
    "piggy_bank_id": 1,
    "amount": 100.00,
    "note": "Monthly savings"
  }'
```

---

## 🚢 Deployment

### Render.com
```bash
# Start command
uvicorn app.main:app --host 0.0.0.0 --port 10000
```

### Railway.app
```bash
# Set these environment variables in Railway dashboard:
# - DATABASE_URL (PostgreSQL service)
# - SECRET_KEY
# - ALGORITHM
# - ACCESS_TOKEN_EXPIRE_MINUTES
# - REFRESH_TOKEN_EXPIRE_DAYS

# Start command
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

### Docker-based VPS
```bash
# Build and push image to registry
docker build -t your-registry/piggybank-api:latest .
docker push your-registry/piggybank-api:latest

# On VPS, use docker-compose with production settings
docker-compose -f docker-compose.prod.yml up -d
```

### Pre-deployment Checklist
- [ ] Set `DEBUG=False` in production
- [ ] Generate strong `SECRET_KEY` (use `python -c "import secrets; print(secrets.token_urlsafe(32))"`)
- [ ] Use PostgreSQL (not SQLite) in production
- [ ] Set up automated backups for the database
- [ ] Configure HTTPS/SSL certificates
- [ ] Run database migrations before deployment
- [ ] Set appropriate resource limits on containers
- [ ] Implement rate limiting on API endpoints

---

## 📋 What I Learned

This project served as a comprehensive exploration of modern backend development:

### Technical Skills
- **Web Framework**: Building sync APIs with FastAPI and understanding ASGI principles
- **Database**: Designing relational schemas, managing migrations with Alembic, and ORM relationships
- **Authentication**: Implementing JWT-based auth with access/refresh token patterns and secure password handling
- **Architecture**: Applying layered architecture principles for maintainability and scalability
- **Containerization**: Packaging applications with Docker and orchestrating services with Docker Compose

### Backend Engineering Principles
- Clean code organization with separation of concerns
- Error handling and validation at multiple layers
- Configuration management for different environments
- Database transaction management and consistency
- API design following REST conventions and best practices

### Development Practices
- Version control with modular code structure
- Environment-based configuration
- Documentation through OpenAPI/Swagger
- Containerized development workflow
- Database migration strategies for safe deployments

This project demonstrates the practical application of enterprise backend engineering patterns in a realistic scenario.

---

## 📝 Future Enhancements

- **Testing**: Unit and integration tests with pytest and test coverage reports
- **Async Database**: Async SQLAlchemy with async drivers for improved concurrency
- **Caching**: Redis integration for token blacklisting and data caching
- **Monitoring**: Logging with structured JSON logs and application monitoring
- **Analytics**: Monthly savings reports, spending patterns, and goal tracking
- **Advanced Features**: Budget goals with alerts, recurring transactions, transaction categorization
- **Security**: Email verification, two-factor authentication (2FA), rate limiting, API key management
- **Performance**: Pagination for large datasets, query optimization, database indexing
- **CI/CD**: GitHub Actions for automated testing, linting, and deployment workflows

---

## 📞 Support & Contributing

For questions or contributions, please visit the [GitHub repository](https://github.com/Credence1289/PiggyBank-Personal-saving-tracker-Fast-Api).

---

## 👨‍💻 Author

**Vinayak Dewoolkar**  
Backend Developer | FastAPI | API Architecture Enthusiast


---

**Last Updated**: June 2026  
**Status**: Active Development
