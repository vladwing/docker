#!/bin/sh
export PYTHONPATH=/opt/graphite/webapp:/opt/graphite/webapp/graphite
export DJANGO_SETTINGS_MODULE=graphite.settings
CHECK_FILE=/opt/graphite/post-setup-complete
LOCAL=/usr/local/bin
GUNICORN=/usr/bin/gunicorn

( if [ -z "$(ls -A /opt/graphite/conf)" ]; then
	echo "[Graphite] /opt/graphite/conf is empty. Copying default config."
	cp /opt/graphite/initconfig/* /opt/graphite/conf
fi ) && ( if [ ! -f "$CHECK_FILE" ] ; then
    echo "[graphite-web] Initializing local_settings.py and 'admin' user"
    $LOCAL/setup-local-settings.py && $LOCAL/post-setup-graphite-web.py && touch $CHECK_FILE
fi ) && (
    echo "[graphite-web] starting ..."
    $GUNICORN graphite_wsgi:application --workers 4 --bind 127.0.0.1:8000
)
