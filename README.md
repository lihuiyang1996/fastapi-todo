📝 FastAPI Todo
A full-featured Todo API application built with FastAPI, Tortoise ORM, and JWT Authentication. Designed for clean architecture, modularity, and extensibility. Includes features like user management, token-based authentication, task CRUD, pagination, and optional Docker support.

🚀 Features
Module	Description
✅ Auth	JWT-based login system, token generation
✅ User System	User registration, password change, info
✅ Task System	Create, read, update, delete (CRUD) for todos
✅ Multi-user	Each user has their own todo list
✅ Pagination	List APIs support page/size and filters
✅ Permission	Route protection with token verification
✅ Dockerized	Ready-to-run with Docker & Docker Compose
✅ API Docs	Swagger UI & ReDoc auto-generated docs

📁 Project Structure
.
├── app/
│   ├── api/             # API routes
│   ├── controllers/     # Business logic (controller/repository)
│   ├── schemas/         # Pydantic models for requests/responses
│   ├── models/          # Tortoise ORM database models
│   ├── core/            # Config, auth, and shared dependencies
│   └── utils/           # Helper functions
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

⚙️ Quick Start

1. Clone the repository
git clone https://github.com/lihuiyang1996/fastapi-todo.git
cd fastapi-todo

2. Environment setup
Copy and modify .env.example:
DATABASE_URL=sqlite://db.sqlite3
JWT_SECRET_KEY=your-secret-key
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=60
SQLite is used for development. For production, use PostgreSQL or MySQL.

3. Run locally
Create a virtual environment and install dependencies:
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Run the app:
uvicorn app.main:app --reload

Access API docs:
Swagger UI: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc

4. Run with Docker
docker-compose up --build
The app will be available at http://localhost:8000.

🔐 Authentication
JWT access tokens are issued upon login (/api/user/access_token)

Include token in headers for protected endpoints:
token: <JWT_TOKEN>

✅ API Endpoints (Examples)

✅ POST /api/user/access_token
Obtain a JWT access token (Login)

✅ GET /api/user/userinfo
Retrieve current user info (requires login)

✅ POST /api/user/update_password
Change password for logged-in user

✅ GET /api/user/list
List users with pagination and filters (admin use)

✅ POST /api/user/create
Create a new user (admin only)

✅ DELETE /api/user/delete?user_id=1
Delete a user by ID (admin only)

✅ POST /api/user/reset_password
Reset user password to default (admin only)

📝 Todo Endpoints
✅ GET /api/todo/
List todos for current user with optional pagination

✅ POST /api/todo/
Create a new todo task

✅ GET /api/todo/{id}
Retrieve details of a specific task

✅ PUT /api/todo/{id}
Update an existing task

✅ DELETE /api/todo/{id}
Delete a task

🧪 Development Tips
Format code with black, isort, or ruff

Use descriptive commit messages (e.g., fix: handle login edge case)

Write unit tests for core logic

Develop in branches and submit pull requests

📈 Future Improvements (Ideas)
Add labels/tags to tasks

Support file uploads (e.g., task attachments)

Add notification/email reminder system

Integrate Celery for background tasks

Add Web frontend (React/Vue/Svelte)

🙌 Contributions
Feel free to open issues or submit PRs to improve the project!