import os
import time
from subprocess import run

def submit(user, user_file):
    user_job = '{"localFile" : "userfile", "destFile" : "primes.py"}'.replace("userfile", user_file)
    run(['bash', 'submit.sh', user_file, user_job, user])

def create_temp_copy(user, code):
    fname = user + "_primes.py"
    f = open(fname, 'w')
    f.write(code)
    f.close()
    return fname

def clean_up(user, fname, tango_output):
    time.sleep(1)
    run(['rm', fname])
    time.sleep(1)
    path = tango_output+user+'.out'
    run(['rm', path])
