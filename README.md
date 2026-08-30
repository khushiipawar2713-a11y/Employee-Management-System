# Employee Management System

## Project Overview

Employee Management System is a web-based HR management application developed using Django and Python. 
The system helps organizations manage employee records efficiently with authentication, employee operations, analytics dashboard, and reporting features.

---

## Tech Stack

- Python
- Django
- SQLite
- HTML
- CSS
- Bootstrap
- JavaScript

---

## Features

### Authentication
- User Login
- User Logout

### Employee Management
- Add Employee
- View Employee Details
- Update Employee
- Delete Employee
- Search Employee
- Pagination

### Employee Profile
- Upload Employee Photo
- Display Employee Profile

### Dashboard
- Employee Statistics
- Data Visualization Charts

### Reports
- Export Employee Data to Excel
- Generate Employee PDF Report

---

## Project Screenshots

### Login Page
![Login](screenshots/login.png)

### Dashboard
![Dashboard](screenshots/dashboard.png)

### Employee List
![Employee List](screenshots/employee-list.png)

### Add Employee
![Add Employee](screenshots/add-employee.png)

---

## Project Structure
│
├── employees/
│ ├── models.py
│ ├── views.py
│ ├── forms.py
│ └── urls.py
│
├── core/
│ ├── settings.py
│ └── urls.py
│
├── templates/
├── static/
├── media/
├── db.sqlite3
└── manage.py


## Environment Checks

### 1. Verify Python is installed
```powershell
python --version
```
or
```powershell
python3 --version
```

### 2. Verify pip is installed
```powershell
pip --version
```
or
```powershell
python -m pip --version
```

### 3. Check whether a virtual environment is active
When a virtual environment is active, the shell prompt usually includes the environment name, for example `(venv)`.

To confirm from the command line:
```powershell
where python
where pip
```
If the paths point inside the `venv` folder, the virtual environment is active.

## Virtual Environment Commands

### Create a virtual environment
```powershell
python -m venv venv
```

### Activate the virtual environment (Windows PowerShell)
```powershell
.\venv\Scripts\Activate.ps1
```

### Activate the virtual environment (Windows Command Prompt)
```cmd
venv\Scripts\activate.bat
```

### Deactivate the virtual environment
```powershell
deactivate
```

## Django Project Setup

### Install project dependencies
```powershell
pip install -r requirements.txt
```

If `requirements.txt` does not exist, install Django manually:
```powershell
pip install django
```

### Run Django development server
```powershell
python manage.py runserver
```

## Start a new Django app
Inside the project root:
```powershell
python manage.py startapp <app_name>
```

## Common sanity commands

### List installed packages
```powershell
pip list
```

### Show path to Python interpreter
```powershell
python -c "import sys; print(sys.executable)"
```

### Show Django version
```powershell
python -m django --version
```
