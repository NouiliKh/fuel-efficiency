from database.crud import CRUDFromDf
from database.database import Database
import pandas as pd


if __name__ == "__main__":
    Database.initialise(database="fuel_consumption", user="baya", password="123456789", host="localhost")

    # Load csv to data
    url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data'
    column_names = ['MPG', 'Cylinders', 'Displacement', 'Horsepower', 'Weight',
                    'Acceleration', 'Model Year', 'Origin']

    raw_dataset = pd.read_csv(url, names=column_names,
                              na_values='?', comment='\t',
                              sep=' ', skipinitialspace=True, header=None)

    CRUDFromDf(raw_dataset, 'auto_mg').create_from_file()
