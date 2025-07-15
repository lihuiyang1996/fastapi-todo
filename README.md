# 📝 FastAPI Todo

A full-featured **Todo API application** built with **FastAPI**, **Tortoise ORM**, and **JWT authentication**.  
It supports user authentication, multi-user task management, pagination, Docker deployment, and more.  
Perfect for learning, prototyping, or scaling into a production-ready backend.

---

## 🚀 Features

- ✅ JWT-based user authentication
- ✅ Full CRUD for tasks (todos)
- ✅ Multi-user data isolation
- ✅ Pagination and filters
- ✅ Secure endpoints with dependency injection
- ✅ Async ORM with Tortoise
- ✅ Docker + Docker Compose support
- ✅ Auto-generated interactive API docs (Swagger & ReDoc)

---

## 📁 Project Structure

```
.
├── app/
│   ├── api/             # API routes
│   ├── controllers/     # Business logic / repositories
│   ├── schemas/         # Pydantic models
│   ├── models/          # Tortoise ORM models
│   ├── core/            # Auth, settings, dependencies
│   └── utils/           # Utility functions
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## ⚙️ Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/lihuiyang1996/fastapi-todo.git
cd fastapi-todo
```

---

### 2. Set environment variables

Create and edit a `.env` file or set the following variables:

```env
DATABASE_URL=sqlite://db.sqlite3
JWT_SECRET_KEY=your-secret-key
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

### 3. Run locally

Create virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run the app:

```bash
uvicorn app.main:app --reload
```

Visit API docs:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

---

### 4. Run with Docker

```bash
docker-compose up --build
```

Access the app at: [http://localhost:8000](http://localhost:8000)

---

## 🔐 Authentication

Use JWT tokens to access protected routes.

- Get token via: `POST /api/user/access_token`
- Pass token in header:
  ```
  token: <your-token>
  ```

---

## ✅ API Endpoints (Examples)

### Auth & User

| Method | Endpoint                      | Description                          |
|--------|-------------------------------|--------------------------------------|
| POST   | `/api/user/access_token`      | Obtain JWT token (Login)            |
| GET    | `/api/user/userinfo`          | Get current user info (requires auth) |
| POST   | `/api/user/update_password`   | Change current user password         |
| GET    | `/api/user/list`              | List users with pagination/filtering |
| POST   | `/api/user/create`            | Create a new user (admin)            |
| DELETE | `/api/user/delete?user_id=1`  | Delete a user by ID (admin)          |
| POST   | `/api/user/reset_password`    | Reset user password (admin)          |

---

### Todos

| Method | Endpoint             | Description                        |
|--------|----------------------|------------------------------------|
| GET    | `/api/todo/`         | List todos for current user        |
| POST   | `/api/todo/`         | Create a new todo task             |
| GET    | `/api/todo/{id}`     | Retrieve details of a specific task |
| PUT    | `/api/todo/{id}`     | Update a task                      |
| DELETE | `/api/todo/{id}`     | Delete a task                      |

> All todo endpoints require authentication.

---

## 🧪 Development Tips

- Use `black`, `isort`, or `ruff` for formatting
- Write unit tests for controllers & services
- Use Git branches and semantic commit messages
- Keep `requirements.txt` updated (`pip freeze > requirements.txt`)

---

## 📈 Future Improvements

- Add task categories or labels
- Add file uploads or image support
- Add email/password reset workflow
- Add background tasks with Celery or APScheduler
- Add frontend integration (e.g. React or Vue)

---

## 📚 References

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Tortoise ORM](https://tortoise-orm.readthedocs.io/)
- [Pydantic](https://docs.pydantic.dev/)
- [JWT with FastAPI](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)

---

## 🙌 Contributing

Feel free to open issues or submit pull requests to improve the project.

---
