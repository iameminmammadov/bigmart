import pandas as pd
from datacube_bigmart import config
import os
from os.path import join, exists
import joblib
from datacube_bigmart.version import __version__
import logging
import boto3
import tempfile



class DataManagement():
    def __init__(self, save_file_name=None):
        self.save_file_name = save_file_name
        self.logger = logging.getLogger(__name__)

    def save_pipeline(self, pipeline_to_persist):
        """
        Save the pipeline. Saved pipeline overwrites any previous saved models. By doing so, in the published
        version, there is only one trained model and it's easy to trace it
        :param sklearn object pipeline_to_persist: Passed a built Pipeline, imported from sklearn
        :return: N/A
        """

        save_file_name = f"{config.PIPELINE_SAVE_FILE }{__version__}.pkl"
        s3 = boto3.resource('s3')
        with tempfile.TemporaryFile() as fp:
            joblib.dump(pipeline_to_persist, fp)
            fp.seek(0)
            s3.Bucket('bigmart-trained-models').put_object(Key=save_file_name, Body=fp.read())
        self.logger.info(f"saved pipeline: {save_file_name}")

    def load_pipeline(self):
        """
        Loads the pipeline for further usage
        :param : N/A
        :return pipeline: Returns a pipeline that is a sklearn object
        """
        save_file_name = f"{config.PIPELINE_SAVE_FILE }{__version__}.pkl"
        s3 = boto3.resource('s3')
        with tempfile.TemporaryFile() as fp:
            s3.Bucket('bigmart-trained-models').download_fileobj( Key=save_file_name, Fileobj=fp)
            fp.seek(0)
            pipeline = joblib.load(fp)
        self.logger.info(f"loading pipeline: {save_file_name}")
        return pipeline









