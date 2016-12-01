import os
from subprocess import run

def submit(user, user_file):
    user_job = '{"localFile" : "userfile", "destFile" : "primes.py"}'.replace("userfile", user_file)
    retcode = run(['bash', 'submit.sh', user_file, user_job, user])
    return retcode

