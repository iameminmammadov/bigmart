FROM python:3.6
MAINTAINER Emin Mammadov <emin.e.mammadov@gmail.com>

WORKDIR /opt/datacube_bigmart

ADD ./packages/datacube_bigmart /opt/datacube_bigmart
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt #/opt/datacube_bigmart/

RUN python /opt/datacube_bigmart/setup.py install --force

# Running Python Application
CMD ["python", "/opt/datacube_bigmart/datacube_bigmart/train_pipeline.py"]
