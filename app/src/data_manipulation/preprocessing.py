import pandas as pd
from tensorflow.keras.layers.experimental import preprocessing
import numpy as np


class ConvertCategoryToDummies:
    def __init__(self, column_name):
        self.column_name = column_name

    def fit(self, X, y=None):
        X[self.column_name] = X[self.column_name].map({1: 'USA', 2: 'Europe', 3: 'Japan'})
        X = pd.get_dummies(X, columns=[self.column_name], prefix='', prefix_sep='')
        return X

    def evaluate(self):
        return NotImplemented


class Normalization:
    def __init__(self, number_of_variables):
        self.normalization_layer = preprocessing.Normalization() if number_of_variables > 1 \
            else preprocessing.Normalization(input_shape=[1, ])

    def fit(self, X):
        X = np.array(X)
        self.normalization_layer.adapt(X)
        return self.normalization_layer


class Preprocess:
    def __init__(self, dataset, feature_column, label_column):
        dataset = dataset[feature_column+label_column]
        dataset = dataset.dropna()

        self.X_train = dataset.sample(frac=0.8, random_state=0)
        self.X_test = dataset.drop(self.X_train.index)

        self.y_train = pd.DataFrame([self.X_train.pop(col) for col in label_column]).T
        self.y_test = pd.DataFrame([self.X_test.pop(col) for col in label_column]).T

    def fit(self):
        if 'Origin' in list(self.X_train.columns):
            self.X_train = ConvertCategoryToDummies('Origin').fit(self.X_train)
        normalization_layer = Normalization(self.X_train.shape[1]).fit(self.X_train)
        return self.X_train, self.y_train, normalization_layer

    def evaluate(self):
        if 'Origin' in list(self.X_test.columns):
            self.X_test = ConvertCategoryToDummies('Origin').fit(self.X_test)
        return self.X_test, self.y_test

    @staticmethod
    def predict(X):
        X = X.dropna()
        if 'Origin' in list(X.columns):
            X = ConvertCategoryToDummies('Origin').fit(X)
        return X
