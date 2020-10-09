tar -zcvf datacube_bigmart.tar.gz datacube_bigmart
curl -F package=@datacube_bigmart.tar.gz $PIP_EXTRA_INDEX_URL
