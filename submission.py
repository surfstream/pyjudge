import os
from subprocess import call as run

userArg = "user2"
userFileArg = 'user2_primes.py'
userJobArg = '{"localFile" : "userfile", "destFile" : "primes.py"}'.replace("userfile", userFileArg)
run(['bash', 'submit.sh', userFileArg, userJobArg, userArg])

