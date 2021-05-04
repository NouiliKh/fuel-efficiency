from database.database import Database
from load_csv import load_df_to_postgres
from pipeline_orchestrator.orchestrator import Orchestrator
from database.model_metadata import fetch_model_with_accuracy_threshold
import os


if __name__ == "__main__":
    logs = {}
    database = os.getenv('database', '')
    user = os.getenv('user', '')
    password = os.getenv('password', '')
    host = os.getenv('host', 'localhost')
    # Database.initialise(database=database, user=user, password=password, host=host)
    Database.initialise(database='fuel_consumption', user='baya', password='123456789', host='localhost')
    raw_dataset = load_df_to_postgres()

    # 1 variable
    columns_to_use = ['Horsepower']
    label_columns = ['MPG']

    epochs = 100
    verbose = 0
    validation_split = 0.2
    num_classes = len(label_columns)
    learning_rate = 0.01

    orchestrator = Orchestrator(epochs=epochs, verbose=verbose, validation_split=validation_split,
                                num_classes=num_classes, learning_rate=learning_rate)
    orchestrator.start('1_variable', raw_dataset, columns_to_use, label_columns)

    # multi variable
    columns_to_use = ['Cylinders', 'Displacement', 'Horsepower', 'Weight', 'Acceleration', 'Model Year', 'Origin']
    label_columns = ['MPG']
    orchestrator.learning_rate = 0.001
    orchestrator.start('multi_variable', raw_dataset, columns_to_use, label_columns)

    # Evaluate and compare
    orchestrator.compare_and_evaluate()

    # Get models that were trained in the last week with a Mean Absolute Error (MAE) of less than 2.5
    threshold = 2.5
    result = fetch_model_with_accuracy_threshold(threshold)






