#! /bin/bash -e

cd $(dirname $0)/..

source ./auto/venv/bin/activate

echo 'INFO: render plantuml'

python ./auto/plantuml.py ./content

deactivate
