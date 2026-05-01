# 📋 Team Task Manager

A full-stack web application where users can create projects, assign tasks, and track progress with **role-based access control (Admin/Member)**.

🔗 **Live URL:** [https://task-manager-production-83ee.up.railway.app](https://task-manager-production-83ee.up.railway.app)  
📁 **GitHub Repo:** [https://github.com/akshchaudhary10/Task-Manager](https://github.com/akshchaudhary10/Task-Manager)

---

## 🚀 Key Features

- 🔐 **Authentication** — User Signup & Login
- 👥 **Role-Based Access Control** — Admin and Member roles
- 📁 **Project Management** — Create and manage projects with teams
- ✅ **Task Management** — Create, assign, and track tasks
- 📊 **Dashboard** — View tasks by status, overdue tasks at a glance
- 🌐 **REST APIs** — Full API support using Django REST Framework
- 🔒 **CORS Support** — Cross-origin requests handled securely

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Django 6.0.4 |
| API | Django REST Framework 3.17.1 |
| Database | SQLite |
| Server | Gunicorn |
| Deployment | Railway |
| Frontend | HTML, CSS, JavaScript |

---

## 📁 Project Structure

```
Task-Manager/
├── core/          # Project settings and configuration
├── users/         # Authentication & user management
├── projects/      # Project & team management
├── tasks/         # Task creation & tracking
├── frontend/      # HTML templates
├── manage.py
├── requirements.txt
└── Procfile
```

---

## ⚙️ How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/akshchaudhary10/Task-Manager.git
cd Task-Manager
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate      # Windows
# OR
source venv/bin/activate   # Mac/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python manage.py migrate
```

### 5. Create a Superuser (Admin)
```bash
python manage.py createsuperuser
```

### 6. Start the Server
```bash
python manage.py runserver
```

Visit: [http://localhost:8000](http://localhost:8000)

---

## 🌐 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/users/register/` | Register a new user |
| POST | `/api/users/login/` | Login and get token |
| GET | `/api/projects/` | List all projects |
| POST | `/api/projects/` | Create a new project |
| GET | `/api/tasks/` | List all tasks |
| POST | `/api/tasks/` | Create a new task |
| PATCH | `/api/tasks/<id>/` | Update task status |

---

## 👤 Role-Based Access

| Feature | Admin | Member |
|---------|-------|--------|
| Create Project | ✅ | ❌ |
| Assign Tasks | ✅ | ❌ |
| View Tasks | ✅ | ✅ |
| Update Task Status | ✅ | ✅ |
| Manage Members | ✅ | ❌ |

---

## 🚢 Deployment

This app is deployed on **Railway** using Gunicorn as the production server.

```
# Procfile
web: gunicorn core.wsgi --bind 0.0.0.0:$PORT
```

---

## 📦 Dependencies

```
Django==6.0.4
djangorestframework==3.17.1
django-cors-headers==4.9.0
gunicorn==25.3.0
asgiref==3.11.1
sqlparse==0.5.5
```

---

## 👨‍💻 Author

**Aksh Chaudhary**  
GitHub: [@akshchaudhary10](https://github.com/akshchaudhary10)
