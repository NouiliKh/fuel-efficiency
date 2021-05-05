import pandas as pd
from database.auto_mg import create_from_file


def load_csv_to_df():

    # Load csv to data
    url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data'
    # Load data from mirror
    url = 'auto-mpg.data-original.txt'
    column_names = ['MPG', 'Cylinders', 'Displacement', 'Horsepower', 'Weight',
                    'Acceleration', 'Model Year', 'Origin']

    raw_dataset = pd.read_csv(url, names=column_names,
                              na_values='?', comment='\t', header=None,
                              sep=' ', skipinitialspace=True)

    return raw_dataset.reset_index(drop=True)


def load_df_to_postgres():
    raw_dataset = load_csv_to_df()
    create_from_file(raw_dataset)
    return raw_dataset
