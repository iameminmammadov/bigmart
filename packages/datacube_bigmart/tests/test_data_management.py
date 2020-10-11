import boto3
import pandas as pd
import pandas.testing as pd_testing
import os


def test_load_dataset():
    s3 = boto3.client('s3')

    obj_train = s3.get_object(Bucket='bigmart-dataset', Key='Train.csv')
    loaded_train = pd.read_csv(obj_train['Body'])

    obj_test = s3.get_object(Bucket='bigmart-dataset', Key='Test.csv')
    loaded_test = pd.read_csv(obj_test['Body'])

    CWD = os.getcwd()
    path_to_train = os.path.join(CWD, 'datacube_bigmart/datacube_bigmart/datasets/Train.csv')
    path_to_test = os.path.join(CWD, 'datacube_bigmart/datacube_bigmart/datasets/Test.csv')
    train_true = pd.read_csv(path_to_train)
    test_true = pd.read_csv(path_to_test)
    pd_testing.assert_frame_equal(loaded_train, train_true)
    pd_testing.assert_frame_equal(loaded_test, test_true)






