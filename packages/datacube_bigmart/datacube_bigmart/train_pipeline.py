import logging
from sklearn.model_selection import train_test_split
from datacube_bigmart.pipeline import BigMartPipeline
from datacube_bigmart.data_management import DataManagement
from datacube_bigmart import config
from sklearn.metrics import mean_absolute_error as mae
from datacube_bigmart.version import __version__
import pandas as pd
import numpy as np
from xgboost import XGBRegressor
from sklearn.ensemble import RandomForestRegressor
import boto3
import warnings
warnings.filterwarnings("ignore")

logger = logging.getLogger(__name__)


def run_training():

    dm = DataManagement()
    bmp = BigMartPipeline()
    s3 = boto3.client('s3')

    obj = s3.get_object(Bucket='bigmart-dataset', Key='Train.csv')
    data = pd.read_csv(obj['Body'])

    X = data.iloc[:, :-1]
    y = data['Item_Outlet_Sales']
    train_ratio = 0.70

    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        test_size=1 - train_ratio,
                                                        random_state=42)
    '''
    search_space = [{
        'clf': [RandomForestRegressor()],
        'clf__n_estimators': [int(x) for x in np.linspace(start = 0, stop = 100, num = 50)],
        'clf__max_features': ['auto', 'sqrt'],
        'clf__max_depth': [int(x) for x in np.linspace(0, 50, num = 10)],
        'clf__min_samples_split': [2, 5, 10],
        'clf__min_samples_leaf': [1, 2, 4],
        'clf__bootstrap': [True, False]
            },
        {
        'clf': [XGBRegressor()],
        'clf__max_depth': [3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        'clf__min_child_weight': np.arange(0.0001, 0.5, 0.001),
        'clf__gamma': np.arange(0.0,40.0,0.005),
        'clf__learning_rate': np.arange(0.0005,0.3,0.0005),
        'clf__subsample': np.arange(0.01,1.0,0.01),
        'clf__colsample_bylevel': np.round(np.arange(0.1,1.0,0.01)),
        'clf__colsample_bytree': np.arange(0.1,1.0,0.01)
        }
    ]
    '''
    search_space = [{
        'clf': [RandomForestRegressor()]}]

    pipeline = bmp.pipeline(search_space)
    pipe = pipeline.fit(X_train, y_train)

    y_pred = pipe.predict(X_test)
    print('MAE: ', mae(y_test, y_pred))

    logger.info(f'saving model version: {__version__}')

    dm.save_pipeline(pipeline)



if __name__ == '__main__':
    pipe=run_training()
