import unittest
from load_csv import load_csv_to_df
from data_manipulation.preprocessing import Preprocess


class Tests(unittest.TestCase):

    def test_if_feature_and_label_size_match_after_preprocessing(self):
        raw_dataset = load_csv_to_df()
        columns_to_use = ['Horsepower']
        label_columns = ['MPG']
        preprocessor = Preprocess(dataset=raw_dataset, feature_column=columns_to_use, label_column=label_columns)
        X, y, normalization_layer = preprocessor.fit()
        X_test, y_test = preprocessor.evaluate()
        assert X.shape[0] == y.shape[0]
        assert X_test.shape[0] == y_test.shape[0]


if __name__ == '__main__':
    unittest.main()
