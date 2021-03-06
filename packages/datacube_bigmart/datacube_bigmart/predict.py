from datacube_bigmart.data_management import DataManagement
from datacube_bigmart import config
import pandas as pd
from datacube_bigmart.version import __version__ as model_version

import logging

_logger = logging.getLogger(__name__)


def make_prediction(test_data):
    dm = DataManagement()
    X_test = test_data.copy()

    _pipe = dm.load_pipeline()
    y_pred = pd.DataFrame(_pipe.predict(X_test))

    _logger.info(f"Predictions are made with model version: {model_version}")
    results = {"predictions": y_pred, "version": model_version}
    return results
'''
import boto3
s3 = boto3.client('s3')
obj_test = s3.get_object(Bucket='bigmart-dataset', Key='Test.csv')
loaded_test = pd.read_csv(obj_test['Body'])
make_prediction(loaded_test)
'''
