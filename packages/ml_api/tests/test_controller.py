from datacube_bigmart import config
from datacube_bigmart.data_management import DataManagement
from datacube_bigmart.version import __version__
from ml_api._version import __version__ as api_version
import boto3
import pandas as pd

import json


def test_health_endpoint(flask_test_client):
    response = flask_test_client.get('/health')
    assert response.status_code == 200


def test_version_endpoint(flask_test_client):
    response = flask_test_client.get('/version')
    assert response.status_code == 200

    response_json = json.loads(response.data)
    assert response_json[0]['api_version'] == api_version
    assert response_json[1]['model_version'] == __version__


def test_prediction_endpoints(flask_test_client):
    s3 = boto3.client('s3')

    obj_test = s3.get_object(Bucket='bigmart-dataset', Key='Test.csv')
    input_data = pd.read_csv(obj_test['Body'])
    json_data = input_data.to_json(orient='records')

    response = flask_test_client.post('/v1/predict',
                                      data=json.dumps(json_data),
                                      content_type='application/json')
    assert response.status_code == 200

    response_json = json.loads(response.data)
    assert response_json['version'] == __version__
