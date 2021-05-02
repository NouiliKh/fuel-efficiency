import tensorflow as tf
from tensorflow.keras import layers
import numpy as np


class Model:
    def __init__(self,  normalization_layer):
        self.epochs = 100
        self.verbose = 1
        self.validation_split = 0.2
        self.num_classes = 1
        self.learning_rate = 0.1

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
        history = self.model.fit(X, y, epochs=self.epochs, verbose=self.verbose, validation_split=self.validation_split)
        return history

    def predict(self, x):
        self.model.predict(x)
