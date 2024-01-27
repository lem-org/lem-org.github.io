#! /bin/bash -ex

cd $(dirname $0)/..

find ./content -regex ".*\.raw\.md" | entr ./auto/preproccess.sh
