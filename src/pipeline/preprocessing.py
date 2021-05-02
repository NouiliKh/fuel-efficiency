import pandas as pd
from tensorflow.keras.layers.experimental import preprocessing
import numpy as np


class ExtractSelectedFeatures:
    def __init__(self, X, columns):
        self.X = X[columns]


class HandleMissingData:
    def __init__(self, X, y=None):
        self.X = X
        self.y = y

    def fit(self):
        self.X = self.X.dropna()
        return self.X

    def evaluate(self):
        return NotImplemented


class ConvertCategoryToDummies:
    def __init__(self, X, column_name):
        self.X = X
        self.column_name = column_name

    def fit(self):
        self.X[self.column_name]= self.X[self.column_name].map({1: 'USA', 2: 'Europe', 3: 'Japan'})
        self.X = pd.get_dummies(self.X, columns=[self.column_name], prefix='', prefix_sep='')
        return self.X

    def evaluate(self):
        return NotImplemented


class Normalization:
    def __init__(self, X):
        self.X = np.array(X)
        self.normalization_layer = preprocessing.Normalization() if X.shape[1] > 1 \
            else preprocessing.Normalization(input_shape=[1, ])

    def fit(self):
        self.normalization_layer.adapt(self.X)
        return self.normalization_layer


class Preprocess:
    def __init__(self, dataset, feature_column, label_column):
        dataset = dataset[feature_column+label_column]
        self.X_train = dataset.sample(frac=0.8, random_state=0)
        self.X_test = dataset.drop(self.X_train.index)

        self.y_train = pd.DataFrame([self.X_train.pop(col) for col in label_column]).T
        self.y_test = pd.DataFrame([self.X_test.pop(col) for col in label_column]).T

    def fit(self):
        X = HandleMissingData(self.X_train).fit()
        if 'Origin' in list(X.columns):
            X = ConvertCategoryToDummies(X, 'Origin').fit()
        normalization_layer = Normalization(X).fit()
        return X, self.y_train, normalization_layer

    def evaluate(self):
        return NotImplemented