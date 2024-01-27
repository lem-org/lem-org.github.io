#! /bin/bash -ex

cd $(dirname $0)/..

hugo server --disableFastRender --gc
