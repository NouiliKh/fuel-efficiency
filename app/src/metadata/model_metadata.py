from datetime import datetime
from database.model_metadata import create_from_dict


def model_metadata(version, id_preprocessing_metadata, epochs, validation_split, learning_rate, mae_test,
                   mae_train, saved_model_name):
    """
    used to collect model_metadata data and transform it into a dict
    ...
    Attributes
    ----------
    version : txt
        model version
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
    create_from_dict({'version': version, 'preprocessing_metadata_id': id_preprocessing_metadata, 'epochs': epochs,
                      'validation_split': validation_split, 'learning_rate': learning_rate, 'mae_test': mae_test,
                      'mae_train': mae_train, 'model_name': saved_model_name, 'created_at': datetime.now()})