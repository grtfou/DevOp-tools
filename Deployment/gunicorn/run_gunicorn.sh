#!/bin/bash
# Ref: http://docs.gunicorn.org/en/stable/deploy.html
WEBDIR=/work/your_web_app
PROJECT_NAME=website

GUNICORN=/usr/local/bin/gunicorn
PID=$WEBDIR/gunicorn.pid

PYTHON_PATH=/home/www-data/.pyenv/versions/3.5.2/bin/python

LOGFILE=$WEBDIR/logs/gunicorn.log
LOGDIR=$(dirname $LOGFILE)

set -e
DJANGODIR=$WEBDIR/$PROJECT_NAME
DJANGO_WSGI=$PROJECT_NAME.wsgi
DJANGO_SETTINGS_MODULE=$PROJECT_NAME.settings.py
GUNICORN_CONFIG=$WEBDIR/config.py

cd $DJANGODIR

test -d $LOGDIR || mkdir -p $LOGDIR
exec $GUNICORN -D -c $GUNICORN_CONFIG \
     --pid=$PID \
     --log-level=debug  \
     --log-file=$LOGFILE \
     --pythonpath $PYTHON_PATH \
     $DJANGO_WSGI 2>>$LOGFILE

