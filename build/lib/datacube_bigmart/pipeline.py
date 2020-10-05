import logging

from sklearn.model_selection import RandomizedSearchCV
from sklearn.pipeline import Pipeline

from datacube_bigmart import preprocessing as pp

_logger = logging.getLogger(__name__)

class BigMartPipeline():
    def pipeline(self, search_space):
        if len(search_space[0]['clf']) == 0:
            raise ValueError('Pass an estimator')
        else:
            pipe = Pipeline(steps=[('imputation_step', pp.BigMartFeatureImputation()),
                                   ('cleaning_step', pp.BigMartNameCleaning()),
                                   ('encoding_step', pp.BigMartFeatureEncoding()),
                                   ('clf', search_space[0]['clf'][0])
                                   ])
            rscv = RandomizedSearchCV(pipe, search_space, cv=5, n_jobs=-1, return_train_score=False, verbose=3)
            return rscv





