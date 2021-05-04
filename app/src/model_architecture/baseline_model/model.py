import tensorflow as tf
from tensorflow.keras import layers
from model_architecture.custom_callbacks import ExecutionTimeCallbackFit, ExecutionTimeCallbackEvaluate


class Model:
    """
    A class used to create the baseline model.
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
    def __init__(self, normalization_layer, epochs=100, verbose=0, validation_split=0.2, num_classes=1,
                 learning_rate=0.01):
        self.epochs = epochs
        self.verbose = verbose
        self.validation_split = validation_split
        self.num_classes = num_classes
        self.learning_rate = learning_rate
        self.normalization_layer = normalization_layer
        self.model = self.initialize_model()

    def initialize_model(self):
        """
        used to initialize the model and compile it.
        """
        model = tf.keras.Sequential([
            self.normalization_layer,
            layers.Dense(units=self.num_classes)
        ])
        model.compile(optimizer=tf.optimizers.Adam(learning_rate=self.learning_rate), loss='mean_absolute_error')
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
        # Since I wanted to log the execution time as well as the loss and val_loss, I created a custom callback function.
        custom_callback = ExecutionTimeCallbackFit()
        self.model.fit(X, y, epochs=self.epochs, verbose=self.verbose, validation_split=self.validation_split
                       , callbacks=[custom_callback])
        return custom_callback.history

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
        return self.model.predict(x)
