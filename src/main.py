from database.database import Database
from load_csv import load_df_to_postgres
from pipeline_orchestrator.orchestrator import Orchestrator


if __name__ == "__main__":
    logs = {}
    Database.initialise(database="fuel_consumption", user="baya", password="123456789", host="localhost")
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





