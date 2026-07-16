import os
from .settings import *
import dj_database_url

# Set debug to False in production
DEBUG = False

# Use Render-provided hostname or default to localhost
ALLOWED_HOSTS = [os.environ.get('RENDER_EXTERNAL_HOSTNAME', 'localhost')]

# Recommended for CSRF protection (e.g. for forms)
CSRF_TRUSTED_ORIGINS = [
    'https://' + os.environ.get('RENDER_EXTERNAL_HOSTNAME', 'localhost')
]

# Secret key must be set in environment variable
SECRET_KEY = os.environ.get('SECRET_KEY', 'unsafe-default')

# Middleware for production
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ← fixed missing comma
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

# Static files config for WhiteNoise
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Parse DATABASE_URL from Render
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}

# CORS for React frontend (update to your actual frontend URL)
CORS_ALLOWED_ORIGINS = [
    "https://your-react-frontend.onrender.com",  # ✅ Replace with your frontend URL
    # "http://localhost:3000",  # optional for local dev
]
