import time
import tensorflow as tf
from tensorflow.keras.callbacks import Callback


class ExecutionTimeCallback(Callback):

    def __init__(self):
        self.history = {'loss':[], 'val_loss':[], 'execution_time': []}

        # use this value as reference to calculate cummulative time taken
        self.timetaken = tf.timestamp()

    def on_batch_end(self, batch, logs={}):
        self.history['loss'].append(logs.get('loss'))

    def on_epoch_end(self, epoch, logs={}):
        self.history['val_loss'].append(logs.get('val_loss'))
        self.history['execution_time'].append(tf.timestamp() - self.timetaken)

    def on_test_end(self, logs=None):
        self.history['loss'].append(logs.get('loss'))
        self.history['execution_time'].append(tf.timestamp() - self.timetaken)

