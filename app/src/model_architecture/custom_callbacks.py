import time
import tensorflow as tf
from tensorflow.keras.callbacks import Callback

# For some reason, I had to split the custom callback since I am using validation set while
# training to avoid duplicated values

class ExecutionTimeCallbackFit(Callback):
    """
    Creates a custom callback that logs the loss, val_loss and execution time for each epoch while training.
    ...
    Methods
    -------
    on_epoch_end(epochs, logs)
        saves val_loss, loss and execution_time at the end of each epoch.
    """
    def __init__(self):
        self.history = {'loss':[], 'val_loss':[], 'execution_time': []}
        # use this value as reference to calculate cummulative time taken
        self.timetaken = tf.timestamp()

    def on_epoch_end(self, epoch, logs={}):
        self.history['val_loss'].append(logs.get('val_loss'))
        self.history['loss'].append(logs.get('loss'))
        self.history['execution_time'].append(tf.timestamp() - self.timetaken)


class ExecutionTimeCallbackEvaluate(Callback):
    """
    Creates a custom callback that logs the loss, val_loss and execution time for each epoch while evaluating.
    ...
    Methods
    -------
    on_test_end(epochs, logs)
        saves val_loss, loss and execution_time at the end of testing.
    """
    def __init__(self):
        self.history = {'loss': 0, 'execution_time': 0}

        # use this value as reference to calculate cummulative time taken
        self.timetaken = tf.timestamp()

    def on_test_end(self, logs=None):
        self.history['execution_time'] = tf.timestamp() - self.timetaken
        self.history['loss'] = logs.get('loss')