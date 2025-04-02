import os
from pathlib import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+xs&t=sns36(==ob@00ntub0vx5zlh!ft2ldw16z(bmid7^#ko'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
LOGIN_REDIRECT_URL = '/'  # Or the path you want after login
ALLOWED_HOSTS = []
# Tenant model configuration
TENANT_MODEL = 'tenants.Client'  # Ensure the correct path to the model


# Shared apps that are common across all tenants
SHARED_APPS = [
    'django.contrib.contenttypes',  # This should only be in SHARED_APPS
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.staticfiles',  # Static files are shared
    'django_tenants',  # django-tenants must be in shared apps
]

# Tenant-specific apps (each tenant gets its own apps)
TENANT_APPS = [
    'students',  # Your tenant-specific apps
    'teachers',
    'school',  # Other apps related to your school management system
    # Add more apps if necessary
]

INSTALLED_APPS = [
    # Shared apps
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_tenants',
    # Tenant-specific apps
    'student',
    'teacher',
    'school',
    'home_auth',  # Custom authentication app
    'tenants',  # Tenant management app
    # Any other apps
]

MIDDLEWARE = [
    'django_tenants.middleware.TenantMiddleware',  # This should be first
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL configuration
ROOT_URLCONF = 'Home.urls'

# Templates configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Home.wsgi.application'

DATABASE_ROUTERS = ['django_tenants.routers.TenantSyncRouter']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    },
}



# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Static root for deployment
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Authentication settings
AUTH_USER_MODEL = 'home_auth.CustomUser'  # Adjust 'home_auth' to the app where CustomUser is defined
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # Default backend
)

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')  # Get email from environment variable
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')  # Get password from environment variable

