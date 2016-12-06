"""
Helper moduel to handle temporary files as well as provide a clean call to
interface with Tango server for submissions.
"""


import time
from subprocess import run


def submit(user, user_file):
    """
    Funtion to alter the a string in order to make the appropriate funtion call
    in order to submit a job to the tango server.
    """
    user_job = '{"localFile" : "userfile", "destFile" : "primes.py"}'.replace(
        "userfile", user_file)
    run(['bash', 'submit.sh', user_file, user_job, user])


def create_temp_copy(user, code):
    """
    Function to create the temporary file from user submited code. In order to
    create jobs for the tango server and/or find similar code to provide a hint
    for the client.
    """
    fname = user + "_primes.py"
    user_file = open(fname, 'w')
    user_file.write(code)
    user_file.close()
    return fname


def clean_up(user, fname, tango_output):
    """
    Function containing clean up code, to remove output file once displayed to
    client to reduce storage, as well as allow Tango server some leeway to
    properly terminate before clean up.
    """
    time.sleep(1)
    run(['rm', fname])
    time.sleep(1)
    path = tango_output + user + '.out'
    run(['rm', path])
