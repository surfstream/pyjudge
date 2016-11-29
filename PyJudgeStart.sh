#! /bin/bash

python3 app.py &

cd ../Tango
source bin/activate
python restful-tango/server.py 5001 &
deactivate
