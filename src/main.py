from database.crud import CRUDFromDf
from database.database import Database
from pipeline.preprocessing import Preprocess
from model_architecture.baseline_model.model import Model as BaselineModel
from model_architecture.deep_neural_network.model import Model as DNNModel
import pandas as pd


if __name__ == "__main__":
    Database.initialise(database="fuel_consumption", user="baya", password="123456789", host="localhost")

    # Load csv to data
    url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data'
    column_names = ['MPG', 'Cylinders', 'Displacement', 'Horsepower', 'Weight',
                    'Acceleration', 'Model Year', 'Origin']

    raw_dataset = pd.read_csv(url, names=column_names,
                              na_values='?', comment='\t',
                              sep=' ', skipinitialspace=True, header=None)

    # CRUDFromDf(raw_dataset, 'auto_mg').create_from_file()


    # Train baseline model with 1 variable
    # Preprocess

    preprocessor = Preprocess(dataset=raw_dataset, feature_column=['Horsepower'], label_column=['MPG'])
    X, y, normalization_layer = preprocessor.fit()
    X_test, y_test = preprocessor.evaluate()
    X_prediction = Preprocess.predict(X_test)

    # Fit model
    baseline_1_variable = BaselineModel(normalization_layer)
    baseline_1_variable.fit(X, y)
    baseline_1_variable.evaluate(X_test, y_test)
    baseline_1_variable.predict(X_test)

    # Fit DNN
    DNN_1_variable = DNNModel(normalization_layer)
    DNN_1_variable.fit(X, y)
    DNN_1_variable.evaluate(X_test, y_test)


    columns_to_use = ['Cylinders', 'Displacement', 'Horsepower', 'Weight', 'Acceleration', 'Model Year', 'Origin']
    # Train baseline model with multi variable
    X, y, normalization_layer = Preprocess(dataset=raw_dataset,
                                           feature_column=columns_to_use, label_column=['MPG']).fit()
    # Test

    # BaselineModel(normalization_layer).fit(X, y)
    DNNModel(normalization_layer).fit(X, y)

