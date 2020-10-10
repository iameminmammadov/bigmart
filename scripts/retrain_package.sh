#!/usr/bin/env bash
BASE_DIR=$(pwd)
cd '..'
cd "$BASE_DIR/packages/datacube_bigmart"
echo "Changing directory"
pwd
pip install --upgrade pip
python setup.py install --force
