from tensorflow.keras import layers
import tensorflow as tf
from model_architecture.custom_callbacks import ExecutionTimeCallback


class Model:

    def __init__(self,  normalization_layer):
        self.validation_split = 0.2
        self.verbose = 0
        self.epochs = 100
        self.num_classes = 1
        self.learning_rate = 0.001
        self.normalization_layer = normalization_layer
        self.model = self.initialize_model()

    def initialize_model(self):
        model = tf.keras.Sequential([
            self.normalization_layer,
            layers.Dense(64, activation='relu'),
            layers.Dense(64, activation='relu'),
            layers.Dense(self.num_classes)
        ])
        model.compile(loss='mean_absolute_error', optimizer=tf.keras.optimizers.Adam(self.learning_rate))
        return model

    def fit(self, X, y):
        custom_callback = ExecutionTimeCallback()
        self.model.fit(X, y, epochs=self.epochs, verbose=self.verbose, validation_split=self.validation_split
                       , callbacks=[custom_callback])
        return custom_callback.history

    def evaluate(self, X, y):
        custom_callback = ExecutionTimeCallback()
        self.model.evaluate(X, y, callbacks=[custom_callback])
        return custom_callback.history

    def predict(self, x):
        return self.model.predict(x)
