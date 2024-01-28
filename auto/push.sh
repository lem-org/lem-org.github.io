#! /bin/bash -ex

cd $(dirname $0)/..

./auto/preproccess.sh

git add .

git commit --amend --no-edit

git push origin main --force-with-lease
