"""
WSGI configuration for PythonAnywhere deployment.
Copy this content to your PythonAnywhere WSGI configuration file.
"""

import os
import sys

# Add your project directory to the Python path
# Replace 'yourusername' with your actual PythonAnywhere username
path = "/home/kim34/mysite"
if path not in sys.path:
    sys.path.append(path)

# Set the Django settings module
os.environ["DJANGO_SETTINGS_MODULE"] = "core.settings_pa"

# Import Django's WSGI application
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
