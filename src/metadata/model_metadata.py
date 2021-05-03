from datetime import datetime
from database.model_metadata import create_from_dict


class PreprocessingMetadata:
    def __init__(self, epochs, validation_split, learning_rate, mae_test, mae_train):

        self.updated_time = datetime.now()
        create_from_dict({'epochs': epochs, 'validation_split': validation_split,
                          'learning_rate': learning_rate, 'mae_test': mae_test, 'mae_train': mae_train,
                          'created_at': self.updated_time})