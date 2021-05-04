import tensorflow as tf
from tensorflow.keras import layers
from model_architecture.custom_callbacks import ExecutionTimeCallbackFit, ExecutionTimeCallbackEvaluate


class Model:
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
        model = tf.keras.Sequential([
            self.normalization_layer,
            layers.Dense(units=self.num_classes)
        ])
        model.compile(optimizer=tf.optimizers.Adam(learning_rate=self.learning_rate), loss='mean_absolute_error')
        return model

    def fit(self, X, y):
        custom_callback = ExecutionTimeCallbackFit()
        self.model.fit(X, y, epochs=self.epochs, verbose=self.verbose, validation_split=self.validation_split
                       , callbacks=[custom_callback])
        return custom_callback.history

    def evaluate(self, X, y):
        custom_callback = ExecutionTimeCallbackEvaluate()
        self.model.evaluate(X, y, callbacks=[custom_callback])
        return custom_callback.history

    def predict(self, x):
        return self.model.predict(x)
