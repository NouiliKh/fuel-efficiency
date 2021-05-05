from data_manipulation.preprocessing import Preprocess
from metadata.preprocessing_metadata import preprocessing_metadata
from metadata.model_metadata import model_metadata
from model_architecture.baseline_model.model import Model as BaselineModel
from model_architecture.deep_neural_network.model import Model as DNNModel
from model_architecture.models_evaluation import EvaluateAndCompare


class Orchestrator():
    """
     A class used to create the pipeline orchestrator and run it.
     ...
     Attributes
     ----------
     epochs : int
         number of epochs the model is trained with
     verbose : bool
         omits the model log while training
     validation_split : float
         the train/test data split
     num_classes: int
         number of output_nodes
     learning_rate: float
         learning rate value

     Methods
     -------
     start()
         Executes every step in the pipeline.
     compare_and_evaluate()
         Compare and evaluates the results of every model.
     """
    def __init__(self, epochs=100, verbose=0, validation_split=0.2, num_classes=1, learning_rate=0.01):
        self.epochs = epochs
        self.verbose = verbose
        self.validation_split = validation_split
        self.num_classes = num_classes
        self.learning_rate = learning_rate
        self.logs = {}

    def start(self, plot_name, raw_dataset, columns_to_use, label_columns):
        preprocessor = Preprocess(dataset=raw_dataset, feature_column=columns_to_use, label_column=label_columns)
        X, y, normalization_layer = preprocessor.fit()
        X_test, y_test = preprocessor.evaluate()
        id_preprocessing_metadata = preprocessing_metadata(X, y, X_test, y_test)

        # Baseline model
        baseline = BaselineModel(normalization_layer, epochs=self.epochs, verbose=self.verbose,
                                 validation_split=self.validation_split, num_classes=self.num_classes,
                                 learning_rate=self.learning_rate)
        baseline_train, saved_model_name = baseline.fit(X, y)
        baseline_evaluate = baseline.evaluate(X_test, y_test)

        self.logs['baseline_' + plot_name + '_train'] = baseline_train
        self.logs['baseline_' + plot_name + '_evaluate'] = baseline_evaluate

        model_metadata('baseline', id_preprocessing_metadata, self.epochs, self.validation_split, self.learning_rate,
                       baseline_train['loss'][-1], baseline_evaluate['loss'], saved_model_name)

        # DNN
        dnn = DNNModel(normalization_layer, epochs=self.epochs, verbose=self.verbose,
                       validation_split=self.validation_split, num_classes=self.num_classes,
                       learning_rate=self.learning_rate)
        dnn_train, saved_model_name = dnn.fit(X, y)
        dnn_evaluate = dnn.evaluate(X_test, y_test)
        self.logs['dnn_' + plot_name + '_train'] = dnn_train
        self.logs['dnn_' + plot_name + '_evaluate'] = dnn_evaluate

        model_metadata('dnn', id_preprocessing_metadata, self.epochs, self.validation_split, self.learning_rate,
                       dnn_train['loss'][-1], dnn_evaluate['loss'], saved_model_name)

    def evaluate(self, raw_dataset, columns_to_use, label_columns, model_name):
        preprocessor = Preprocess(dataset=raw_dataset, feature_column=columns_to_use, label_column=label_columns)
        X, y, normalization_layer = preprocessor.fit()
        X_test, y_test = preprocessor.evaluate()

        dnn = DNNModel(normalization_layer, epochs=self.epochs, verbose=self.verbose,
                       validation_split=self.validation_split, num_classes=self.num_classes,
                       learning_rate=self.learning_rate, model_name=model_name)
        dnn.evaluate(X_test, y_test)

    def compare_and_evaluate(self):
        EvaluateAndCompare(self.logs).plots()
        EvaluateAndCompare(self.logs).compare()
