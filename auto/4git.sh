#! /bin/bash -ex

git config user.email lem-org@outlook.com
git config core.quotepath false

git submodule update --remote --merge
