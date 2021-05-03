import pandas as pd
from database.crud import CRUDFromDf


def load_csv_to_df():
    # Load csv to data
    url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data'
    column_names = ['MPG', 'Cylinders', 'Displacement', 'Horsepower', 'Weight',
                    'Acceleration', 'Model Year', 'Origin']

    raw_dataset = pd.read_csv(url, names=column_names,
                              na_values='?', comment='\t',
                              sep=' ', skipinitialspace=True, header=None)
    return raw_dataset


def load_df_to_postgres():
    raw_dataset = load_csv_to_df()
    # CRUDFromDf(raw_dataset, 'auto_mg').create_from_file()
    return raw_dataset