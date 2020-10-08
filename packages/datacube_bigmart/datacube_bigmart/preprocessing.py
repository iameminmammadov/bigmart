from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import OrdinalEncoder
import pandas as pd
import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer


class BigMartNameCleaning(BaseEstimator, TransformerMixin):
    def __init__(self):
        super().__init__()

    def fit(self, X, y=None, **kwargs):
        return self

    def transform(self, X, y=None, **kwargs):
        # Do Transformation Here
        if X is None:
            raise ValueError('Input the data')
        X = X.copy()
        X = self.predict(X)
        return X

    def predict(self, X, y=None, **kwargs):
        if X is None:
            raise ValueError('Input the data')
        X = X.copy()

        for value in X['Item_Identifier']:
            if 'FD' in value:
                X['Item_Identifier'] = X['Item_Identifier'].replace(value, 'FD')
            elif 'DR' in value:
                X['Item_Identifier'] = X['Item_Identifier'].replace(value, 'DR')
            elif 'NC' in value:
                X['Item_Identifier'] = X['Item_Identifier'].replace(value, 'NC')

        X['Item_Fat_Content'].replace({'reg': 'Regular',
                                       'low fat': 'Low Fat',
                                       'LF': 'Low Fat'}, inplace=True)
        X['Item_Fat_Content'][X['Item_Identifier'].str.contains('NC')] = 'Non Consumable'
        return X


class BigMartFeatureEncoding(BaseEstimator, TransformerMixin):

    def __init__(self):
        super().__init__()

    def fit(self, X, y=None, **kwargs):
        if X is None:
            raise ValueError('Input the data')

        self.cat_list = list(
            X.select_dtypes(include=['category', 'object', 'bool']).columns)

        for col in self.cat_list:
            X[col] = X.astype('object')

        self.X_encoding = X.select_dtypes(include=[np.object])
        self.X_rest = X.select_dtypes(exclude=[np.object])

        self.oe = OrdinalEncoder()
        self.oe.fit(self.X_encoding)

        return self

    def transform(self, X, y=None, **kwargs):
        # Do Transformation Here
        if X is None:
            raise ValueError('Input the data')
        X = X.copy()
        X = self.predict(X)
        return X

    def predict(self, X, y=None, **kwargs):
        # Include all other columns
        self.cat_list = list(
            X.select_dtypes(include=['category', 'object', 'bool']).columns)

        for col in self.cat_list:
            X[col] = X.astype('object')

        self.X_encoding = X.select_dtypes(include=[np.object])
        self.X_rest = X.select_dtypes(exclude=[np.object])

        self.X_encoded = pd.DataFrame(self.oe.transform(self.X_encoding),
                                      columns=self.X_encoding.columns)

        self.X_encoded.reset_index(drop=True, inplace=True)
        self.X_rest.reset_index(drop=True, inplace=True)

        X_out = pd.concat([self.X_encoded, self.X_rest], axis=1)
        X = X_out.reindex(X.columns, axis=1)
        return X


class BigMartFeatureImputation(BaseEstimator, TransformerMixin):
    def __init__(self):
        super().__init__()

    def fit(self, X, y=None, **kwargs):
        # Only numerical here
        if X is None:
            raise ValueError('Input the data')

        self.X_numerical = X.select_dtypes(include='number')
        self.imputer_num = IterativeImputer()
        self.imputer_num.fit(self.X_numerical)

        return self

    def predict(self, X, y=None, **kwargs):
        X = X.copy()
        # transform here

        self.cat_list = list(
            X.select_dtypes(include=['category', 'object', 'bool']).columns)

        for col in self.cat_list:
            X[col] = X.astype('object')

        self.X_categorical = X.select_dtypes(include=[np.object])
        self.X_numerical = X.select_dtypes(include=['number'])

        self.X_numerical_encoded = pd.DataFrame(self.imputer_num.transform(self.X_numerical),
                                                columns=self.X_numerical.columns)

        self.X_categorical = self.X_categorical.fillna('Missing')

        self.X_numerical_encoded.reset_index(drop=True, inplace=True)
        self.X_categorical.reset_index(drop=True, inplace=True)

        X_out = pd.concat([self.X_numerical_encoded, self.X_categorical], axis=1)
        X = X_out.reindex(X.columns, axis=1)

        return X

    def transform(self, X, y=None, **kwargs):
        # Do Transformation Here
        if X is None:
            raise ValueError('Input the data')
        X = X.copy()
        X = self.predict(X)
        return X
