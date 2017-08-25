#! /bin/sh

### BEGIN INIT INFO
# Provides:          nginx
# Source from: http://www.linode.com/docs/assets/1139-init-deb.sh
# Required-Start:    $all
# Required-Stop:     $all
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: starts the nginx web server
# Description:       starts nginx using start-stop-daemon
### END INIT INFO
### CMD
#sudo mv init-deb.sh /etc/init.d/nginx
#sudo chmod +x /etc/init.d/nginx
#sudo /usr/sbin/update-rc.d -f nginx defaults
###-CMD

PATH=/usr/local/nginx/sbin:/sbin:/bin:/usr/sbin:/usr/bin
DAEMON=/usr/local/nginx/sbin/nginx
SERVICE_NAME=nginx
DAEMON_OPTS="-c /usr/local/nginx/nginx.conf"
PID_PATH="/usr/local/nginx/logs/$SERVICE_NAME.pid"


test -x $DAEMON || exit 0

# Include nginx defaults if available
if [ -f /etc/default/nginx ] ; then
        . /etc/default/nginx
fi

set -e

case "$1" in
  start)
        echo -n "Starting $SERVICE_NAME... \n"

        {
            start-stop-daemon --start --quiet --pidfile $PID_PATH \
                --exec $DAEMON -- $DAEMON_OPTS  && echo "Success \n"
        } || {
            echo "Fail \n"
        }
        ;;
  stop)
        echo -n "Stopping $SERVICE_NAME... \n"
        {
            start-stop-daemon --stop --quiet --pidfile $PID_PATH \
                --exec $DAEMON  && echo "Success \n"
        } || {
            echo "Fail \n"
        }
        ;;
  restart|force-reload)
        echo -n "Restarting $SERVICE_NAME... \n"

        {
            start-stop-daemon --stop --quiet --pidfile $PID_PATH --exec $DAEMON \
                && echo "Stop service \n"
        } || {
            echo "Stop service fail \n"
        }

        sleep 1

        {
            start-stop-daemon --start --quiet --pidfile $PID_PATH --exec $DAEMON \
                -- $DAEMON_OPTS  && echo "Start service \n"
        } || {
            echo "Start service fail \n"
        }
        ;;
  reload)
        echo -n "Reloading $SERVICE_NAME configuration... \n"
        {
            start-stop-daemon --stop --signal HUP --quiet --pidfile  $PID_PATH \
                --exec $DAEMON  && echo "Success \n"
        } || {
            echo "Reloading fail \n"
        }
        ;;
  *)
        N=/etc/init.d/$SERVICE_NAME
        echo "Usage: $N {start|stop|restart|reload|force-reload}" >&2
        exit 1
        ;;
esac

exit 0
