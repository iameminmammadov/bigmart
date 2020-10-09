GEMFURY_URL=$PIP_EXTRA_INDEX_URL

tar -zcvf datacube_bigmart.tar.gz datacube_bigmart
curl -F package=@datacube_bigmart.tar.gz GEMFURY_URL
