from flask import Blueprint, request, jsonify
from ml_api.api.config import get_logger
from ml_api._version import __version__ as api_version
from datacube_bigmart.version import __version__ as model_version
from datacube_bigmart.predict import make_prediction
import json
import simplejson
import pandas as pd

prediction_app = Blueprint('prediction_app', __name__)

_logger = get_logger(logger_name=__name__)


@prediction_app.route('/health', methods=['GET'])
def health():
    if request.method == 'GET':
        _logger.info('health status OK')
        return 'ok'


@prediction_app.route('/version', methods=['GET'])
def version():
    if request.method == 'GET':
        return jsonify({'api_version': api_version},
                       {'model_version': model_version})


@prediction_app.route('/v1/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        json_data = request.get_json()
        _logger.debug(f'Inputs: {json_data}')

        normalized_str = simplejson.dumps(json_data, ignore_nan=True)
        data_js_dict = simplejson.loads(normalized_str)
        a_json = json.loads(data_js_dict)
        test_data = pd.DataFrame.from_dict(a_json, orient="columns")

        results = make_prediction(test_data)

        predictions = results['predictions'].values.tolist()
        model_version = results['version']

        return jsonify({'predictions': predictions,
                        'version': model_version
                        })
