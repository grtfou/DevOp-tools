#!/bin/sh

### BEGIN INIT INFO
# Provides:          uwsgi
# Required-Start:    $all
# Required-Stop:     $all
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: starts the uwsgi app server
# Description:       starts uwsgi app server using start-stop-daemon
### END INIT INFO

PATH=/opt/uwsgi:/sbin:/bin:/usr/sbin:/usr/bin
DAEMON=/home/www-data/.pyenv/versions/2.7.9/bin/uwsgi
INI_PATH=/work/systools/uwsgi/server.ini
PID_PATH=/work/systools/uwsgi/log/uwsgi.pid

OWNER=www-data
SERVICE_NAME=uwsgi

test -x $DAEMON || exit 0

# Include uwsgi defaults if available
if [ -f /etc/default/uwsgi ] ; then
        . /etc/default/uwsgi
fi

set -e

DAEMON_OPTS="--ini $INI_PATH"

case "$1" in
  start)
        echo -n "Starting $SERVICE_NAME... \n"

        {
            start-stop-daemon --start --chuid $OWNER:$OWNER --user $OWNER \
                --exec $DAEMON -- $DAEMON_OPTS  && echo "Success \n"
        } || {
            echo "Fail \n"
        }
        ;;
  stop)
        echo -n "Stopping $SERVICE_NAME... \n"
        {
            start-stop-daemon --signal 3 --user $OWNER --quiet --retry 2 --stop \
                --exec $DAEMON  && echo "Success \n"
        } || {
            echo "Fail \n"
        }
        ;;
  reload)
        echo -n "Reload $SERVICE_NAME... \n"
        killall -1 $DAEMON
        echo "Success \n"
        ;;
  force-stop)
        echo -n "Force stop $SERVICE_NAME... \n"
        killall -9 $DAEMON
        echo "Success \n"
        ;;
  force-reload)
        echo -n "Force reload $SERVICE_NAME... \n"
        killall -15 $DAEMON
        echo "Success \n"
        ;;
  restart)
        echo -n "Restarting $SERVICE_NAME... \n"

        {
            start-stop-daemon --signal 3 --user $OWNER --quiet --retry 2 --stop \
                --exec $DAEMON  && echo "Stop service \n"
        } || {
            echo "Stop service fail \n"
        }

        sleep 1

        {
            start-stop-daemon --user $OWNER --start --quiet --chuid $OWNER:$OWNER \
                --exec $DAEMON -- $DAEMON_OPTS  && echo "Start service \n"
        } || {
            echo "Start service fail \n"
        }
        ;;
  status)
        killall -10 $DAEMON
        ;;
  *)
        N=/etc/init.d/$SERVICE_NAME
        echo "Usage: $N {start|stop|restart|reload|force-stop|force-reload|status}" >&2
        exit 1
        ;;
esac

exit 0
