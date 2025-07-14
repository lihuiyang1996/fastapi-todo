# FastAPI User Management System

This project is a backend RESTful API built with **FastAPI**, **Tortoise ORM**, and **SQLite**, providing basic user management functionalities.

## 🚀 Features

- View user list with pagination and search
- Create, update, and delete users
- Reset user passwords
- Automatically managed timestamps (created_at, updated_at)
- Asynchronous database operations with Tortoise ORM

## 🛠 Tech Stack

- Python 3.10+
- FastAPI
- Tortoise ORM
- SQLite (for local development)
- Pydantic

## 📂 Project Structure

.
├── main.py # Application entry point
├── users.py # User API routes
├── admin.py # User model
├── base.py # Base model and mixins
├── app/
│ ├── controllers/ # Business logic (user_controller etc.)
│ ├── schemas/ # Pydantic request/response models
│ ├── settings/ # Configuration management
│ └── core/ # App initialization: routers, middlewares, etc.

## 📦 Install Dependencies

Use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

pip install -r requirements.txt
▶️ Run the App
uvicorn main:app --reload --port 9999
Access the app at: http://127.0.0.1:9999
API documentation: http://127.0.0.1:9999/docs

✅ API Endpoints (Examples)
GET /api/user/list: List users with pagination and filters

POST /api/user/create: Create a new user

DELETE /api/user/delete?user_id=1: Delete a user by ID

POST /api/user/reset_password: Reset user password to default