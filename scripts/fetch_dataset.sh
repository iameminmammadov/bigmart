#!/usr/bin/env bash
echo "Downloading from Kaggle"
kaggle datasets download -d brijbhushannanda1979/bigmart-sales-data -p packages/datacube_bigmart/datacube_bigmart/datasets/

echo "Unzipping the package"
unzip -o packages/datacube_bigmart/datacube_bigmart/datasets/bigmart-sales-data.zip -d packages/datacube_bigmart/datacube_bigmart/datasets/

BASE_DIR=$(pwd)
cd "$BASE_DIR/packages/datacube_bigmart/datacube_bigmart/datasets/"
cd .

echo "Uploading to S3"
python upload_s3.py



