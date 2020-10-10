from os.path import join
import pandas as pd
import os

pd.options.display.max_rows = 100
pd.options.display.max_columns = 100

PACKAGE_ROOT = os.getcwd()
TRAINED_MODEL_DIR = join(PACKAGE_ROOT, 'datacube_bigmart/trained_models')
DATASET_DIR = join(PACKAGE_ROOT, 'datacube_bigmart/datasets')

TESTING_DATA_FILE = 'Test.csv'
TRAINING_DATA_FILE = 'Train.csv'
TARGET = 'Item_Outlet_Sales'


PIPELINE_SAVE_FILE = "BigMart_fitted_pipeline"
