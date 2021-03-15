import os
import django
from django.core import asgi

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapps.settings')
django.setup()

application = asgi.get_asgi_application()