from datetime import datetime
from database.preprocessing_metadata import create_from_dict


def preprocessing_metadata(X, y, X_test, y_test):
    """
    used to collect preprocessing_metadata data and transform it into a dict
    ...
    Attributes
    ----------
    X : df
        training data
    y: df
        label data
    X_test: df
        testing data
    y_label: df
        label of the testing data
    """
    number_of_rows_train = X.shape[0]
    size_train = int(X.memory_usage(index=False).sum())

    number_of_rows_test = X_test.shape[0]
    size_test = int(X_test.memory_usage(index=False).sum())

    number_features = X.shape[1]
    number_of_output_nodes = y.shape[1]

    updated_time = datetime.now()
    new_id = create_from_dict({'number_rows_train': number_of_rows_train, 'number_rows_test': number_of_rows_test,
                               'size_train': size_train, 'size_test': size_test, 'number_features': number_features,
                               'number_output_nodes': number_of_output_nodes, 'created_at': updated_time})
    return new_id

