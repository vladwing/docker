#!/bin/sh

echo "Starting StatsD..."
cd /srv/statsd && node stats.js /srv/statsd/config.js
