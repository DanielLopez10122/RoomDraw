# in project root: `gunicorn wsgi.gunicorn`
from app import api

application = api.api
