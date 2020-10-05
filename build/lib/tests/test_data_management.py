from unittest import TestCase
import numpy as np
import pandas as pd
import pandas.testing as pd_testing
from datacube_bigmart.preprocessing import DataManagement


def gen_data():
    random_frame_train = pd.DataFrame(np.ones([10, 5]))
    random_frame_test = pd.DataFrame(np.random.rand(10,5))
    return random_frame_train, random_frame_test



class TestLoadData(TestCase):
    def test_load_dataset(self):
        loaded_train, loaded_test = dm.load_dataset('Train.csv', 'Test.csv')
        train_true = pd.read_csv(config.TRAINING_DATA_FILE)
        test_true = pd.read_csv(config.TESTING_DATA_FILE)
        pd_testing.assert_frame_equal(loaded_train, train_true)
        pd_testing.assert_frame_equal(loaded_test, test_true)






