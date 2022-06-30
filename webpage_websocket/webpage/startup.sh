#! /bin/bash
python ./manage.py makemigrations
python ./manage.py migrate
nohup uwsgi --socket :8001 --module webpage.wsgi --py-autoreload 1 --logto /tmp/mylog.log & daphne -b 0.0.0.0 -p 3001 --ping-interval 10 --ping-timeout 120 webpage.asgi:application
