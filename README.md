
# Django-Auto-Staff: Streamlining Data and Email Management with Precision  
Django-Auto-Staff is a versatile and robust web application designed for advanced operations, making data and email management effortless. Whether you’re dealing with bulk data import/export or tracking the effectiveness of your email campaigns, this application has you covered

## Features
- Seamless Data Import/Export: Effortlessly import data from CSV files into any database table and export it back when needed for reporting or backups.
- Bulk Email Automation: Send personalized bulk emails to users with just a few clicks, streamlining communication.
- Email Tracking Insights: Monitor your email campaigns with precise tracking—know who opens your emails and which links are clicked, with open and click-through rates displayed in real time.

## Prerequisites

Before setting up this project, ensure that you have the following installed on your machine:

- Python 3.12
- Redis server
- Django 5
- Celery 5.4.0

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/CodeWithNasirr/Django-Auto-Staff.git
cd Command
```

### 2. Create a Virtual Environment

Set up a virtual environment for Python dependencies:

```bash
python3 -m venv venv
source venv/bin/activate  # For Linux/Mac
# OR
venv\Scripts\activate  # For Windows
```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file should contain:
```
Django==4.2
celery==5.4.0
django-anymail==12.0
beautifulsoup4==4.12.3
```

### 4. Install and Configure Redis & Celery

Make sure Redis is installed and running:

- For **Linux**:  
  ```bash
  sudo apt install redis
  sudo service redis-server start
  ```

- For **Mac**:  
  Install via Homebrew:
  ```bash
  brew install redis
  brew services start redis
  ```

- For **Windows**:  
  Download Redis for Windows from the official repository [here](https://github.com/microsoftarchive/redis/releases).

#
Make sure Celery is installed and running:

- For **Linux**:  
  ```bash
  install- sudo pip install celery
  Running- celery -A app worker -l info
  ```

- For **Mac**:  
  ```bash
  install- pip install celery
  Running- celery -A app worker -l info
  ```

- For **Windows**:  
  ```bash
    install- pip install celery
    Running- celery -A app worker -l info -P eventlet 
  ```



### 5. Configure Django Settings

In `Command/settings.py`, ensure the following settings are added for **Celery** and **anymail**:

```python
INSTALLED_APPS = [
    # Other installed apps...
    "Email",
    "Home",
    "Upload",  
]

WSGI_APPLICATION = 'Command.wsgi.application'

ANYMAIL = {
    'BREVO_API_KEY': config('BREVO_API_KEY'),
    'DEBUG_API_REQUESTS': True,  # Enable detailed request/response logging
}

EMAIL_BACKEND = "anymail.backends.brevo.EmailBackend"
EMAIL_USE_TLS = True

# EMAIL_BACKEND = config('EMAIL_BACKEND')
# EMAIL_HOST = config('EMAIL_HOST')
# EMAIL_PORT = config('EMAIL_PORT',cast=int)
# EMAIL_USE_TLS = True
EMAIL_HOST_USER=config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD=config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL="Automate with Django <skofficial665@gmail.com>"



CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'


CSRF_TRUSTED_ORIGINS = ['ngrok http 8000 link']

BASE_URL = "ngrok http 8000 link"

```

### 6. Setup Database and Migrate

Run the following commands to create the database and migrate the models:

```bash
python manage.py makemigrations 
python manage.py migrate
```

### 9. Run Django Development Server

Run the Django development server:

```bash
python manage.py runserver
```

### 10. Run Custom Command 



```bash
python manage.py cmd-name(export.py)
```
```
Command/
│
├── Home/                         # Django First App
    ├── managemnet/               # Django Custom Command
            ├── commands
                    ├── export.py  
│   ├── migrations/               # Django migrations
│   ├── static/                   # Static files (CSS, JS, Images)
│   ├── templates/                # HTML templates for the frontend
│   ├── views.py                  # View logic (if any)
│   ├── models.py                 # Order and Pizza models
│   └── urls.py                   # URL r



```
### Directory Structure
```
Command/
│
├── Home/                         # Django First App
    ├── managemnet/               # Django Custom Command
            ├── commands
                    ├── export.py  
│   ├── migrations/               # Django migrations
│   ├── static/                   # Static files (CSS, JS, Images)
│   ├── templates/                # HTML templates for the frontend
│   ├── views.py                  # View logic (if any)
│   ├── models.py                
│   └── urls.py
├── Email/                        # Django Second App
│   ├── migrations/               # Django migrations
│   ├── static/                   # Static files (CSS, JS, Images)
│   ├── templates/                # HTML templates for the frontend
│   ├── views.py                  # View logic (if any)
│   ├── models.py                 
│   └── urls.py    
│
├── Command/                    # Main project folder
│   ├── asgi.py                 # ASGI configuration 
│   ├── wsgi.py                 # wsgi configuration
│   ├── settings.py             # Project settings
│   └── urls.py                 # Main project URL routing
│
└── manage.py                   # Django management script
```

## Testing

1. Add an order using the Django admin interface or Django shell.
2. Open a WebSocket client and connect to the WebSocket URL with the order ID.
3. Change the order status from the admin panel or shell and see real-time updates reflected in the WebSocket client.