import pytest
import pandas as pd
import pandas.testing as pd_testing
from datacube_bigmart.data_management import DataManagement



def test_load_dataset():
    dm = DataManagement()

    loaded_train, loaded_test = dm.load_dataset('Train.csv', 'Test.csv')
    train_true = pd.read_csv('./datacube_bigmart/datasets/Train.csv')
    test_true = pd.read_csv('./datacube_bigmart/datasets/Test.csv')
    pd_testing.assert_frame_equal(loaded_train, train_true)
    pd_testing.assert_frame_equal(loaded_test, test_true)






