#!/bin/bash
set -e

echo "Watching for SASS conversion"
sass --watch static/sass/:static/css/ &
python app.py

while true; do
  sleep 1
done
