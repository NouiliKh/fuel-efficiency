from database.database import Database
from data_manipulation.preprocessing import Preprocess

from load_csv import load_df_to_postgres
from model_architecture.baseline_model.model import Model as BaselineModel
from model_architecture.deep_neural_network.model import Model as DNNModel
from model_architecture.models_evaluation import EvaluateAndCompare

if __name__ == "__main__":
    logs = {}
    Database.initialise(database="fuel_consumption", user="baya", password="123456789", host="localhost")

    raw_dataset = load_df_to_postgres()

    # Preprocess 1 variable data
    columns_to_use = ['Horsepower']
    preprocessor = Preprocess(dataset=raw_dataset, feature_column=columns_to_use, label_column=['MPG'])
    X, y, normalization_layer = preprocessor.fit()
    X_test, y_test = preprocessor.evaluate()

    # Train baseline model with 1 variable
    baseline_1_variable = BaselineModel(normalization_layer)
    baseline_1_variable_train = baseline_1_variable.fit(X, y)
    baseline_1_variable_evaluate = baseline_1_variable.evaluate(X_test, y_test)
    logs['baseline_1_var_train'] = baseline_1_variable_train
    logs['baseline_1_var_evaluate'] = baseline_1_variable_evaluate

    # Train DNN model with 1 variable
    DNN_1_variable = DNNModel(normalization_layer)
    DNN_1_variable_train = DNN_1_variable.fit(X, y)
    DNN_1_variable_evaluate = DNN_1_variable.evaluate(X_test, y_test)
    logs['DNN_1_variable_train'] = DNN_1_variable_train
    logs['DNN_1_variable_evaluate'] = DNN_1_variable_evaluate

    # Preprocess multi variable data
    columns_to_use = ['Cylinders', 'Displacement', 'Horsepower', 'Weight', 'Acceleration', 'Model Year', 'Origin']
    preprocessor = Preprocess(dataset=raw_dataset, feature_column=columns_to_use, label_column=['MPG'])
    X, y, normalization_layer = preprocessor.fit()
    X_test, y_test = preprocessor.evaluate()
    # Train baseline model
    baseline_multi_variable = BaselineModel(normalization_layer)
    baseline_multi_variable_train = baseline_multi_variable.fit(X, y)
    baseline_multi_variable_evaluate = baseline_multi_variable.evaluate(X_test, y_test)
    logs['baseline_multi_variable_train'] = baseline_multi_variable_train
    logs['baseline_multi_variable_evaluate'] = baseline_multi_variable_evaluate

    # Train DNN model with 1 variable
    DNN_multi_variable = DNNModel(normalization_layer)
    DNN_multi_variable_train = DNN_multi_variable.fit(X, y)
    DNN_multi_variable_evaluate = DNN_multi_variable.evaluate(X_test, y_test)
    logs['DNN_multi_variable_train'] = DNN_multi_variable_train
    logs['DNN_multi_variable_evaluate'] = DNN_multi_variable_evaluate

    EvaluateAndCompare(logs).plots()
    EvaluateAndCompare(logs).compare()


