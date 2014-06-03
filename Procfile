web: gunicorn bookprojecta.wsgi

web: python bookprojecta/manage.py collectstatic --noinput; bin/gunicorn_django --workers=4 --bind=0.0.0.0:$PORT bookprojecta/settings.py 