import os, sys
sys.path.insert(0, '/home/u/u98293g8/kachaybeton.rf/public_html/concrete')
sys.path.insert(1, '/home/u/u98293g8/kachaybeton.rf/public_html/venv/lib/python3.6/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()