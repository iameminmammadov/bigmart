GEMFURY_URL=$TOKEN

tar -zcvf datacube_bigmart.tar.gz datacube_bigmart
curl -F package=@datacube_bigmart.tar.gz GEMFURY_URL
