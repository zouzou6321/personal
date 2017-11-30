#!/bin/bash
ps -ef |grep manage.py |awk '{print $2}'|xargs kill -9
nohup python manage.py runserver 2>&1 >> server.log &
nohup python manage.py celery worker --loglevel=info 2>&1 >> celery.log &
nohup python manage.py celery beat --loglevel=info 2>&1 >> celery_beat.log &
nohup python manage.py celery flower 2>&1 >> celery_flower.log &
