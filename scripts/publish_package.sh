tar -zcvf packages/datacube_bigmart/datacube_bigmart.tar.gz packages/datacube_bigmart/datacube_bigmart
curl -F package=@packages/datacube_bigmart/datacube_bigmart.tar.gz $PIP_EXTRA_INDEX_URL
