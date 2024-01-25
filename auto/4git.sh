#! /bin/bash -ex

cd $(dirname $0)/..

git config user.email lem-org@outlook.com
git config core.quotepath false

git submodule update --remote --merge

git config core.hooksPath hooks
cat ./.git/config
