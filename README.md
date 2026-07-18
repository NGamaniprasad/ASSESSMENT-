# Django User Registration System

## Description

Django User Registration System is a web application that allows users to register, view user details, update user information, and delete users.

This project demonstrates basic **CRUD operations** using Django models, forms, views, and templates.

## Features

- User Registration
- View All Registered Users
- Update User Details
- Delete User Details
- Form Validation
- Success Messages

## Technologies Used

- Python
- Django
- HTML
- CSS
- SQLite/MySQL Database

## Project Structure

```
Django-Registration-System/
│
├── app/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│
├── templates/
│   ├── register.html
│   ├── view_users.html
│   ├── update_user.html
│   └── delete_user.html
│
├── manage.py
├── db.sqlite3
└── README.md
```

## CRUD Operations

### Create
- Register a new user using the registration form.

### Read
- View all registered users.

### Update
- Edit existing user information using email.

### Delete
- Remove users from the database.

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/django-registration-system.git
```

### 2. Navigate to Project Folder

```bash
cd django-registration-system
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/Mac**

```bash
source venv/bin/activate
```

### 4. Install Django

```bash
pip install django
```

## Database Setup

Run migrations:

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

## Run the Application

Start the Django server:

```bash
python manage.py runserver
```

Open browser:

```
http://127.0.0.1:8000/
```

## Application Flow

1. User opens registration page.
2. User enters details and submits the form.
3. Data is saved in the database.
4. Registered users are displayed.
5. Users can update or delete records.

## URLs

| URL | Function |
|---|---|
| `/register/` | Register new user |
| `/users/` | View all users |
| `/update/<email>/` | Update user |
| `/delete/<email>/` | Delete user |

## Future Enhancements

- User Login System
- Profile Management
- Search Users
- Pagination
- Admin Dashboard

## License

This project is created for learning purposes.

## Author

N Gamani 
