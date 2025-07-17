# 📝 FastAPI TODO App

A modern asynchronous TODO application built with FastAPI, featuring PostgreSQL, Tortoise ORM, JWT authentication, and Docker Compose support. The project adopts a modular API architecture and is suitable for production deployment or full-stack backend learning.

## 🚀 Tech Stack

- **FastAPI** - High-performance, easy-to-write async web framework  
- **Tortoise ORM** - Asynchronous ORM similar to Django ORM  
- **PostgreSQL** - Stable and powerful relational database  
- **Docker & Docker Compose** - Containerized development and deployment  
- **JWT** - Token-based authentication system  
- **Uvicorn** - High-performance ASGI server  

## 📦 Quick Start (Docker Recommended)

### 1. Clone the repository

```bash
git clone https://github.com/your-username/fastapi-todo-main.git
cd fastapi-todo-main
```

### 2. Configure environment variables

The project includes a pre-defined `.env` file. You can modify it if needed:

```env
# JWT settings
SECRET_KEY=3488a63e1765035d386f05409663f55c83bfae3b3c61a932744b20ad14244dcf
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=10080  # 7 days

# Debug mode
DEBUG=true

# PostgreSQL settings
DB_HOST=db
DB_PORT=5432
DB_USER=fastapi
DB_PASSWORD=secret123
DB_NAME=fastapidb
```

### 3. Start the service

Ensure you have Docker and Docker Compose installed:

```bash
docker-compose up --build
```

App will be available at: `http://localhost:9999`  
API documentation available at:  
- Swagger UI: `http://localhost:9999/docs`  
- ReDoc: `http://localhost:9999/redoc`

## 📂 Project Structure

```
fastapi-todo-main/
├── app/
│   ├── api/                  # API routes
│   │   └── v1/
│   │       ├── apis/         # API management
│   │       ├── todo/         # TODO operations
│   │       ├── roles/        # Role management
│   │       └── auditlog/     # Audit logs
│   ├── controllers/          # Business logic
│   ├── models/               # ORM models
│   └── schemas/              # Request/response models
├── run.py                    # Entry point
├── docker-compose.yml        # Docker Compose file
├── Dockerfile                # Build configuration
├── .env                      # Environment variables
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## 🔐 API Overview

The project auto-generates full API documentation via `/docs`. Key endpoints include:

### ✅ TODO Management

- `GET /todo/list` - Get list of TODO items  
- `POST /todo/create` - Create a new TODO  
- `POST /todo/update` - Update a TODO item  
- `DELETE /todo/delete` - Delete a TODO item  

### ⚙️ API Management

- `GET /apis/list` - List registered APIs (with pagination and search)  
- `GET /apis/get?id=1` - Get details of an API  
- `POST /apis/create` - Create new API  
- `POST /apis/update` - Update API  
- `DELETE /apis/delete?api_id=1` - Delete API  
- `POST /apis/refresh` - Refresh and register all routes  

> All responses are standardized as `Success` or `SuccessExtra` objects for frontend consistency.

## 🗄️ Database & Migrations (Optional)

Tortoise ORM is used for async DB operations. It's recommended to use [aerich](https://tortoise-orm.readthedocs.io/en/latest/migration.html) for migrations.

Sample commands:

```bash
# Initial setup
aerich init -t app.models.TORTOISE_ORM

# Create a migration
aerich migrate

# Apply migration
aerich upgrade
```

Ensure your `.env` file is configured and PostgreSQL is running.

## 🧪 Run Locally (Non-Docker)

For manual local development:

```bash
# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
uvicorn app:app --host 0.0.0.0 --port 9999 --reload
```

Make sure PostgreSQL is installed and your `.env` matches local DB credentials.

## 🐳 Docker Compose Details

The `docker-compose.yml` launches:

- `app`: FastAPI service with auto-reload  
- `db`: PostgreSQL container with persistent volume (`pgdata`)  

It uses the `.env` file for automatic configuration.

## 📝 License

This project is licensed under the MIT License. See LICENSE file for details.