

# **Student Management System**

## **Technologies Used**
- **Backend**: Django (Python), Django ORM
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 
- **Database**: PostgreSQL (or SQLite during development)
- **Version Control**: Git
- **Deployment**: Docker (if Dockerized), Nginx, Gunicorn (for production)
- **Testing**: Django's built-in testing framework

## **Project Structure**
```
student_management_system/
│
├── manage.py               # Django project manager script
├── requirements.txt        # Project dependencies
├── .env                    # Environment variables (add in .gitignore)
├── student_management/     # Main app containing settings, URLs, WSGI
├── students/               # App managing student-related functionalities
├── teachers/               # App managing teacher-related functionalities
└── templates/              # HTML templates
```

## **Installation**
Follow the steps below to get the project up and running on your local machine:

### **1. Clone the Repository**
```bash
git clone https://github.com/schooltimes/student-management-system.git
cd student-management-system
```

### **2. Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Set Up Database**
Make sure to set up your database (e.g., PostgreSQL) and update the `DATABASES` configuration in `student_management/settings.py`.

### **5. Run Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

### **6. Create Superuser**
```bash
python manage.py createsuperuser
```

### **7. Run the Application**
```bash
python manage.py runserver
```
Visit `http://localhost:8000` to access the app.







