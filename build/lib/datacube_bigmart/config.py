from os.path import dirname, abspath, join
import pandas as pd

pd.options.display.max_rows = 100
pd.options.display.max_columns = 100

PACKAGE_ROOT = abspath(dirname(__file__))
TRAINED_MODEL_DIR = join(PACKAGE_ROOT, 'trained_models')
DATASET_DIR = join(PACKAGE_ROOT, 'datasets')

TESTING_DATA_FILE = 'Test.csv'
TRAINING_DATA_FILE = 'Train.csv'
TARGET = 'Item_Outlet_Sales'


PIPELINE_SAVE_FILE = "BigMart_fitted_pipeline"
