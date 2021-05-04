CREATE TABLE IF NOT EXISTS auto_mg (
    id SERIAL NOT NULL PRIMARY KEY,
    mpg FLOAT,
    cylinders INT,
    displacement FLOAT,
    horsepower FLOAT,
    weight FLOAT,
    acceleration FLOAT,
    model_year INT,
    origin INT
);

CREATE TABLE IF NOT EXISTS preprocessing_metadata (
    id SERIAL NOT NULL PRIMARY KEY,
    number_rows_train INT,
    number_rows_test INT,

    size_train FLOAT,
    size_test FLOAT,

    number_features INT,
    number_output_nodes INT,

    created_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS model_metadata (
    id SERIAL NOT NULL PRIMARY KEY,
    epochs INT,
    learning_rate FLOAT,
    validation_split FLOAT,
    mae_test FLOAT,
    mae_train FLOAT,
    created_at TIMESTAMP
);
