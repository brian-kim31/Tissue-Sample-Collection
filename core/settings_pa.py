"""
Django settings for core project on PythonAnywhere.
"""

from .settings import *
import os

# Override settings for PythonAnywhere deployment
DEBUG = False

# PythonAnywhere specific settings
ALLOWED_HOSTS = [
    "yourusername.pythonanywhere.com",  # Replace with your actual PythonAnywhere domain
    "www.yourusername.pythonanywhere.com",
]

# Database - Use SQLite for PythonAnywhere
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Static files configuration for PythonAnywhere
STATIC_URL = "/static/"
STATIC_ROOT = "/home/yourusername/mysite/staticfiles"  # Replace with your actual path

# Media files configuration
MEDIA_URL = "/media/"
MEDIA_ROOT = "/home/yourusername/mysite/media"  # Replace with your actual path

# Security settings for production
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"

# Email configuration for PythonAnywhere
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"  # or your preferred SMTP server
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", "")

# Secret key - make sure to set this as an environment variable
SECRET_KEY = os.environ.get("SECRET_KEY", "your-secret-key-here")
