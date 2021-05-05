import pandas as pd
from tensorflow.keras.layers.experimental import preprocessing
import numpy as np


class ConvertCategoryToDummies:
    """
    A class used to convert categories data to dummies
    ...
    Attributes
    ----------
    column_name : str
        the column name of the category df to convert to dummies
    Methods
    -------
    fit(X, y=None)
        converts a column in an input X to dummies
    """
    def __init__(self, column_name):
        self.column_name = column_name

    def fit(self, X, y=None):
        """
        converts a dataframe column into dummies

        Parameters
        ----------
        X : dataframe
        """
        X[self.column_name] = X[self.column_name].map({1: 'USA', 2: 'Europe', 3: 'Japan'})
        X = pd.get_dummies(X, columns=[self.column_name], prefix='', prefix_sep='')
        return X

    def evaluate(self):
        return NotImplemented


class NormalizeColumnNames:
    """
    A class used to normalize column names. It is helpful if data is ot from multiple sources
    ...
    Attributes
    ----------
    Methods
    -------
    fit(X, y=None)
         normalize column names
    """
    def __init__(self, column_name):
        return NotImplemented

    def fit(self, df):
        """
         normalize column names

        Parameters
        ----------
        df : dataframe
        """
        df.columns = df.columns.str.lower()
        return df

    def evaluate(self):
        return NotImplemented

class Normalization:
    """
    A class used to create normalization layer thanks to the training data
    ...

    Attributes
    ----------
    normalization_layer: the normalization_layer that needed to be fitted

    Methods
    -------
    fit(X, y=None)
        fits the training dataframe and adapting it to the created normalization_layer
    """
    def __init__(self, number_of_variables):
        """
        Parameters
        ----------
        normalization_layer :
            initialized normalized layer
        """
        self.normalization_layer = preprocessing.Normalization() if number_of_variables > 1 \
            else preprocessing.Normalization(input_shape=[1, ])

    def fit(self, X):
        """
        adapting the normalization data with the training set
        Parameters
        ----------
        X : dataframe
        """
        X = np.array(X)
        self.normalization_layer.adapt(X)
        return self.normalization_layer

    def evaluate(self):
        return NotImplemented


class Preprocess:
    """
    A class used to split the dataset into testing and training sets and executes the preprocessing pipeline
    for training, testing and predicting
    ...

    Attributes
    ----------
    X_train: the training set
    X_test: the testing set
    y_train: the training label
    y_test: the testing label

    Methods
    -------
    fit()
        run the preprocessing pipeline for training
    evaluate()
        run the preprocessing pipeline for testing
    predict()
        run the preprocessing pipeline for prediction
    """
    def __init__(self, dataset, feature_column, label_column):
        dataset = dataset[feature_column+label_column]
        dataset = dataset.dropna()

        self.X_train = dataset.sample(frac=0.8, random_state=0)
        self.X_test = dataset.drop(self.X_train.index)

        self.y_train = pd.DataFrame([self.X_train.pop(col) for col in label_column]).T
        self.y_test = pd.DataFrame([self.X_test.pop(col) for col in label_column]).T

    def fit(self):
        """
        run the preprocessing pipeline for training
        """
        if 'Origin' in list(self.X_train.columns):
            self.X_train = ConvertCategoryToDummies('Origin').fit(self.X_train)
        normalization_layer = Normalization(self.X_train.shape[1]).fit(self.X_train)
        return self.X_train, self.y_train, normalization_layer

    def evaluate(self):
        """
        run the preprocessing pipeline for testing
        """
        if 'Origin' in list(self.X_test.columns):
            self.X_test = ConvertCategoryToDummies('Origin').fit(self.X_test)
        return self.X_test, self.y_test

    @staticmethod
    def predict(X):
        """
        run the preprocessing pipeline for prediction
        Parameters
        ----------
        X : dataframe
        """
        X = X.dropna()
        if 'Origin' in list(X.columns):
            X = ConvertCategoryToDummies('Origin').fit(X)
        return X
