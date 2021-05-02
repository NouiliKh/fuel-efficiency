from tensorflow.keras import layers
import tensorflow as tf


class Model:

    def __init__(self,  normalization_layer):
        self.validation_split = 0.2
        self.verbose = 1
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
        self.model.fit(X, y, validation_split=self.validation_split, verbose=self.verbose, epochs=self.epochs)
