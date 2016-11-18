#! /bin/bash

flask_proc=$(ps -u | grep -i "$(pgrep -u ${USER} python)" | grep -i "app" | awk '{print $2}')
kill $flask_proc

tango_proc=$(ps -u | grep -i "$(pgrep -u ${USER} python)" | grep -i "server" | awk '{print $2}')
kill $tango_proc
