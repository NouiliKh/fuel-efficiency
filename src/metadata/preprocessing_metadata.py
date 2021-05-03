from datetime import datetime
from database.preprocessing_metadata import create_from_dict


class PreprocessingMetadata:
    def __init__(self, X, y, X_test, y_test):
        self.number_of_rows_train = X.shape[0]
        self.size_train = int(X.memory_usage(index=False).sum())

        self.number_of_rows_test = X_test.shape[0]
        self.size_test = int(X_test.memory_usage(index=False).sum())

        self.number_features = X.shape[1]
        self.number_of_output_nodes = y.shape[1]

        self.updated_time = datetime.now()
        create_from_dict({'number_rows_train': self.number_of_rows_train, 'number_rows_test': self.number_of_rows_test,
                          'size_train': self.size_train, 'size_test': self.size_test, 'number_features': self.number_features,
                          'number_output_nodes':self.number_of_output_nodes, 'created_at': self.updated_time})
