#!/usr/bin/env bash
BASE_DIR=$(pwd)
cd '..'
cd "$BASE_DIR/packages/datacube_bigmart"
echo "Changing directory"
pwd
pip install --upgrade pip
python setup.py install --force
echo "Retraining step"
python datacube_bigmart/train_pipeline.py
echo "Creating a tar package"
cd '..'
tar -cvzf datacube_bigmart.tar.gz datacube_bigmart
echo "Publishing a package to GemFury"
curl -F package=@datacube_bigmart.tar.gz $PIP_EXTRA_INDEX_URL
