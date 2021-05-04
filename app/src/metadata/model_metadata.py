from datetime import datetime
from database.model_metadata import create_from_dict


def model_metadata(epochs, validation_split, learning_rate, mae_test, mae_train):
    """
    used to collect model_metadata data and transform it into a dict
    ...
    Attributes
    ----------
    epochs : int
        number of epochs
    validation_split: float
        validation split
    learning_rate: float
        model's learning_rate
    mae_test: float
        model's mean squared error with testing data
    mae_train: float
        model's mean squared error with training data
    """
    create_from_dict({'epochs': epochs, 'validation_split': validation_split,
                      'learning_rate': learning_rate, 'mae_test': mae_test, 'mae_train': mae_train,
                      'created_at': datetime.now()})