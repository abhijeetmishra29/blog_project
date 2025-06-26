# Django Blog Project with JWT Authentication

This is a complete blog application built using Django, PostgreSQL, and Django REST Framework. It includes JWT-based user authentication, CRUD operations for blog posts via API, and a simple frontend using Django templates.

---

## 🚀 Features

- JWT-based user registration and login
- PostgreSQL as the backend database
- BlogPost CRUD operations (API + frontend)
- Django REST Framework for API integration
- HTML templates for post listing, detail, and creation
- Admin panel for superuser
- CSRF protection and login required for post creation

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/blog_project.git
cd blog_project
```

### 2. Create a Virtual Environment and Install Dependencies

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
```

### 3. Configure the PostgreSQL Database

- Create a database named `blog_db` in PostgreSQL.
- Then update the following section in `blog_backend/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blog_db',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

- `http://localhost:8000/` → Home Page
- `http://localhost:8000/create/` → Create Post
- `http://localhost:8000/admin/` → Admin Login

---

## 🔗 Frontend Routes

| Route                     | Description                   |
|---------------------------|-------------------------------|
| `/`                       | Home page (all blog posts)    |
| `/create/`                | Create new blog post          |
| `/posts/<id>/view/`       | View individual blog post     |
| `/admin/`                 | Django admin login            |

---

## 📬 API Endpoints (via Django REST Framework)

| Endpoint              | Method         | Description               |
|-----------------------|----------------|---------------------------|
| `/api/register/`      | POST           | User registration         |
| `/api/login/`         | POST           | Obtain JWT token          |
| `/api/token/refresh/` | POST           | Refresh JWT token         |
| `/api/posts/`         | GET / POST     | List or create posts      |
| `/api/posts/<id>/`    | GET / PUT / DELETE | Manage single post   |

> 🛡️ All write operations (POST, PUT, DELETE) require a valid JWT `access` token in the `Authorization: Bearer <token>` header.

---

## ✅ Tech Stack

- Python 3.x
- Django
- PostgreSQL
- Django REST Framework
- SimpleJWT
- HTML + Django Templates

---

## 🙋 Author

**Abhijeet Mishra**  
[GitHub](https://github.com/abhijeetmishra)  
[Email](mailto:your.email@example.com)

---

## 🏁 Project Complete

This project is ready for review. Please feel free to clone, test, or suggest improvements.
