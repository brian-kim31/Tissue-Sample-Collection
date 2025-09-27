# PythonAnywhere Deployment Guide

## Prerequisites
- PythonAnywhere account (already have this)
- Your Django project files

## Step 1: Upload Your Project

1. **Upload files via PythonAnywhere's file browser:**
   - Go to your PythonAnywhere dashboard
   - Navigate to the "Files" tab
   - Upload your project files to `/home/yourusername/mysite/` (replace `yourusername` with your actual username)

2. **Or use git clone (recommended):**
   ```bash
   cd /home/yourusername/mysite/
   git clone https://github.com/brayokenya/Tissue-Sample-Collection.git .
   ```

## Step 2: Set Up Virtual Environment

1. **Create virtual environment:**
   ```bash
   cd /home/yourusername/mysite/
   python3.10 -m venv venv
   source venv/bin/activate
   ```

2. **Install requirements:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements_pa.txt
   ```

## Step 3: Configure Settings

1. **Update settings_pa.py:**
   - Replace `yourusername` with your actual PythonAnywhere username
   - Replace `your-secret-key-here` with a secure secret key
   - Update domain in `ALLOWED_HOSTS`

2. **Set environment variables:**
   ```bash
   # In your .bashrc or .profile
   export SECRET_KEY="your-actual-secret-key-here"
   export EMAIL_HOST_USER="your-email@gmail.com"
   export EMAIL_HOST_PASSWORD="your-app-password"
   ```

## Step 4: Database Setup

1. **Run migrations:**
   ```bash
   cd /home/yourusername/mysite/
   source venv/bin/activate
   python manage.py migrate --settings=core.settings_pa
   ```

2. **Create superuser:**
   ```bash
   python manage.py createsuperuser --settings=core.settings_pa
   ```

3. **Collect static files:**
   ```bash
   python manage.py collectstatic --settings=core.settings_pa
   ```

## Step 5: Configure Web App

1. **Go to "Web" tab in PythonAnywhere dashboard**

2. **Create a new web app:**
   - Choose "Manual Configuration"
   - Select Python 3.10

3. **Configure WSGI file:**
   - Click on the WSGI configuration file link
   - Replace the contents with:

   ```python
   import os
   import sys

   # Add your project directory to the Python path
   path = '/home/yourusername/mysite'
   if path not in sys.path:
       sys.path.append(path)

   # Set the Django settings module
   os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings_pa'

   # Import Django's WSGI application
   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```

4. **Configure static files mapping:**
   - In the "Static files" section:
   - URL: `/static/`
   - Directory: `/home/yourusername/mysite/staticfiles`

5. **Configure media files mapping (if needed):**
   - URL: `/media/`
   - Directory: `/home/yourusername/mysite/media`

## Step 6: Security Settings

1. **Generate a new SECRET_KEY:**
   ```python
   from django.core.management.utils import get_random_secret_key
   print(get_random_secret_key())
   ```

2. **Update settings_pa.py with the new secret key**

3. **Set DEBUG = False in production**

## Step 7: Reload Web App

1. **Click the green "Reload" button** in the Web tab

2. **Check for errors:**
   - View the error log if the site doesn't load
   - Check the server log for any issues

## Step 8: Test Your Application

1. **Visit your site:** `https://yourusername.pythonanywhere.com/`

2. **Test functionality:**
   - Create a superuser account
   - Add sample data
   - Test all CRUD operations

## Troubleshooting

### Common Issues:

1. **Static files not loading:**
   - Ensure `collectstatic` was run
   - Check static files mapping in Web tab
   - Verify `STATIC_ROOT` path in settings

2. **Database errors:**
   - Check migrations were applied
   - Verify database file permissions

3. **Import errors:**
   - Ensure virtual environment is activated
   - Check all dependencies are installed
   - Verify Python path in WSGI file

4. **Permission errors:**
   - Ensure your user owns all files
   - Check file permissions (755 for directories, 644 for files)

### Useful Commands:

```bash
# Check Django version
python -c "import django; print(django.get_version())"

# Check installed packages
pip list

# Run Django shell
python manage.py shell --settings=core.settings_pa

# Check for any issues
python manage.py check --settings=core.settings_pa
```

## Environment Variables (Optional but Recommended)

Create a `.env` file in your project root:
```
SECRET_KEY=your-secret-key-here
DEBUG=False
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

Then update settings_pa.py to use python-decouple:
```python
from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
```

Don't forget to install python-decouple:
```bash
pip install python-decouple
```

## Monitoring

- Check error logs regularly in the Web tab
- Monitor disk usage
- Keep dependencies updated
- Regular backups of your database file
