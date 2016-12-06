#! /bin/bash
: '
This file runs the necessary commands to perform a proper submission on the code
utilizing the provided default code of Tango, due to conflicts calling through
python directly and timeconstraints to fully flesh out with the API to
communicate with pyhton.
'

#store path, used to reference location of temporary code file
path=$(pwd)

#setup to interface with Tango
cd ../Tango
source bin/activate

#check if user has previously submitted a solution for the problem
filepath="courselabs/pyjudge-demo/${1}"
if [ -f $filepath ]
	then
	    #if so delete, since Tango doesn't allow to directly overwrite
		rm $filepath
fi

#"upload" the file to the Tango Server
python clients/tango-rest.py -P 5001 -k "pyjudge" -l "demo" --upload --filename \
"${path}/${1}"

#Create and Run Job:
#run the job on the docker image provided for Tango
python clients/tango-rest.py -P 5001 -k "pyjudge" -l "demo" \
--addJob --infiles \
"$2" '{"localFile" : "autograde-Makefile", "destFile" : "Makefile"}' \
--image "autograding_image" --outputFile "$3.out" --jobname "$3"
#exit script
deactivate

