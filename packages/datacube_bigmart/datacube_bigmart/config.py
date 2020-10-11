from os.path import dirname, abspath, join
import pandas as pd
import os

pd.options.display.max_rows = 100
pd.options.display.max_columns = 100

TARGET = 'Item_Outlet_Sales'

PIPELINE_SAVE_FILE = "BigMart_fitted_pipeline"
