#! /bin/bash

path=$(pwd)
cd ../Tango
source bin/activate
filepath="courselabs/pyjudge-demo/${1}"
if [ -f $filepath ]
	then
		rm $filepath
fi
python clients/tango-rest.py -P 5001 -k "pyjudge" -l "demo" --upload --filename \
"${path}/${1}"

python clients/tango-rest.py -P 5001 -k "pyjudge" -l "demo" \
--addJob --infiles \
"$2" '{"localFile" : "autograde-Makefile", "destFile" : "Makefile"}' \
--image "autograding_image" --outputFile "$3.out" --jobname "$3"
deactivate

