from tensorflow.keras import layers
import tensorflow as tf
from model_architecture.custom_callbacks import ExecutionTimeCallbackFit, ExecutionTimeCallbackEvaluate
from datetime import datetime


class Model:
    """
    A class used to create the dnn model.
    ...
    Attributes
    ----------
    normalization_layer :
        the input normalization layer for the model
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
    initialize_model()
        Initializes the baseline model.
    fit(X,y)
        Fitting the created model with the training data.
    evaluate(X, y)
        Evaluates the model's predictions.
    predict(X)
        Predicts.
    """

    def __init__(self,  normalization_layer, epochs=100, verbose=0, validation_split=0.2, num_classes=1,
                 learning_rate=0.001, model_name='dnn_' + str(datetime.now())):
        self.epochs = epochs
        self.verbose = verbose
        self.validation_split = validation_split
        self.num_classes = num_classes
        self.learning_rate = learning_rate
        self.normalization_layer = normalization_layer
        self.model_name = model_name
        self.checkpoint_path = '../models/' + self.model_name

        self.model = self.initialize_model()

    def initialize_model(self):
        """
        used to initialize the model and compile it.
        """
        model = tf.keras.Sequential([
            self.normalization_layer,
            layers.Dense(64, activation='relu'),
            layers.Dense(64, activation='relu'),
            layers.Dense(self.num_classes)
        ])
        model.compile(loss='mean_absolute_error', optimizer=tf.keras.optimizers.Adam(self.learning_rate))
        return model

    def fit(self, X, y):
        """
        used to train the model.
        ...
        Attributes
        ----------
        X : df
            dataframe to train with
        y: df
            label
        """
        # Since I wanted to log the execution time as well as the loss and val_loss,
        # I created a custom callback function.
        cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=self.checkpoint_path,
                                                         save_weights_only=True, verbose=1)
        custom_callback = ExecutionTimeCallbackFit()
        self.model.fit(X, y, epochs=self.epochs, verbose=self.verbose, validation_split=self.validation_split
                       , callbacks=[custom_callback, cp_callback])
        return custom_callback.history, self.model_name

    def evaluate(self, X, y):
        """
         used to test and evaluate the model.
         ...
         Attributes
         ----------
         X : df
             dataframe to train with
         y: df
             label
         """
        # Since I wanted to log the execution time as well as the loss and I created a custom callback function.
        try:
            self.model.load_weights(self.checkpoint_path)
        except tf.errors.NotFoundError:
            print('File not found (it may be deleted since it was generated in the last container)')
            return
        custom_callback = ExecutionTimeCallbackEvaluate()
        self.model.evaluate(X, y, callbacks=[custom_callback])
        return custom_callback.history

    def predict(self, x):
        """
         used to get predictions from the model.
         ...
         Attributes
         ----------
         X : df/Series
             dataframe/series to get predictions for
         """
        try:
            self.model.load_weights(self.checkpoint_path)
        except tf.errors.NotFoundError:
            print('File not found to load (it may be deleted since it was generated in the last container)')
        self.model.load_weights(self.checkpoint_path)
        return self.model.predict(x)
