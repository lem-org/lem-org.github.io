#! /bin/bash -e

cd $(dirname $0)/..

source ./auto/venv/bin/activate

python ./auto/plantuml.py ./content

deactivate
