import pandas as pd
from datacube_bigmart import config
import os
from os.path import join, exists
import joblib
from datacube_bigmart.version import __version__
import logging


class DataManagement():
    def __init__(self, save_file_name=None):
        self.save_file_name = save_file_name
        self.logger = logging.getLogger(__name__)

    def load_dataset(self, *datasets):
        """Loads dataset.
        :param *args: passed datasets (could train, test or both)
        :return _data_train DataFrame: returns loaded train data set
        :return _data_test DataFrame: returns loaded test data set
        """

        if len(datasets) == 0:
            raise ValueError('Please provide either training, or testing, or both data sets')
        elif len(datasets) == 1:
            if 'Train' in datasets[0]:
                _data_train = pd.read_csv(f"{config.DATASET_DIR}/{datasets[0]}")
                print ('Passed file is a Training set')
                return _data_train
            else:
                _data_test = pd.read_csv(f"{config.DATASET_DIR}/{datasets[0]}")
                print ('Passed file is a Testing set')
                return _data_test
        elif len(datasets) == 2:
            _data_train = pd.read_csv(f"{config.DATASET_DIR}/{datasets[0]}")
            _data_test = pd.read_csv(f"{config.DATASET_DIR}/{datasets[1]}")
            return _data_train, _data_test

    def save_pipeline(self, pipeline_to_persist):
        """
        Save the pipeline. Saved pipeline overwrites any previous saved models. By doing so, in the published
        version, there is only one trained model and it's easy to trace it
        :param sklearn object pipeline_to_persist: Passed a built Pipeline, imported from sklearn
        :return: N/A
        """

        save_file_name = f"{config.PIPELINE_SAVE_FILE }{__version__}.pkl"
        save_path = join(config.TRAINED_MODEL_DIR, save_file_name)
        if not exists(config.TRAINED_MODEL_DIR):
            os.makedirs(config.TRAINED_MODEL_DIR)
        joblib.dump(pipeline_to_persist, save_path)
        print (save_path)
        self.logger.info(f"saved pipeline: {save_file_name}")

    def load_pipeline(self):
        """
        Loads the pipeline for further usage
        :param : N/A
        :return pipeline: Returns a pipeline that is a sklearn object
        """
        save_file_name = f"{config.PIPELINE_SAVE_FILE }{__version__}.pkl"
        file_path = join(config.TRAINED_MODEL_DIR, save_file_name)
        pipeline = joblib.load(file_path)
        self.logger.info(f"loading pipeline: {save_file_name}")
        return pipeline









