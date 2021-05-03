from data_manipulation.preprocessing import Preprocess
from model_architecture.baseline_model.model import Model as BaselineModel
from model_architecture.deep_neural_network.model import Model as DNNModel
from model_architecture.models_evaluation import EvaluateAndCompare


class Orchestrator():
    def __init__(self, epochs=100, verbose=0, validation_split=0.2, num_classes=1,
                 learning_rate=0.01):
        self.epochs = epochs
        self.verbose = verbose
        self.validation_split = validation_split
        self.num_classes = num_classes
        self.learning_rate = learning_rate

        self.logs = {}

    def start(self, model_name, raw_dataset, columns_to_use, label_columns):
        preprocessor = Preprocess(dataset=raw_dataset, feature_column=columns_to_use, label_column=label_columns)
        X, y, normalization_layer = preprocessor.fit()
        X_test, y_test = preprocessor.evaluate()

        # Baseline model
        baseline = BaselineModel(normalization_layer, epochs=self.epochs, verbose=self.verbose,
                                 validation_split=self.validation_split, num_classes=self.num_classes,
                                 learning_rate=self.learning_rate)
        baseline_train = baseline.fit(X, y)
        baseline_evaluate = baseline.evaluate(X_test, y_test)
        self.logs['baseline_' + model_name + '_train'] = baseline_train
        self.logs['baseline_' + model_name + '_evaluate'] = baseline_evaluate

        # DNN
        dnn = DNNModel(normalization_layer, epochs=self.epochs, verbose=self.verbose,
                       validation_split=self.validation_split, num_classes=self.num_classes,
                       learning_rate=self.learning_rate)
        dnn_train = dnn.fit(X, y)
        dnn_evaluate = dnn.evaluate(X_test, y_test)
        self.logs['dnn_' + model_name + '_train'] = dnn_train
        self.logs['dnn_' + model_name + '_evaluate'] = dnn_evaluate

    def compare_and_evaluate(self):
        EvaluateAndCompare(self.logs).plots()
        EvaluateAndCompare(self.logs).compare()
