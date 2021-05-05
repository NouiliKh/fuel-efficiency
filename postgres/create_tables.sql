CREATE TABLE IF NOT EXISTS auto_mg (
    id SERIAL NOT NULL PRIMARY KEY,
    mpg FLOAT,
    cylinders FLOAT,
    displacement FLOAT,
    horsepower FLOAT,
    weight FLOAT,
    acceleration FLOAT,
    model_year FLOAT ,
    origin FLOAT
);

CREATE TABLE IF NOT EXISTS preprocessing_metadata (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    number_rows_train INT,
    number_rows_test INT,

    size_train FLOAT,
    size_test FLOAT,

    number_features INT,
    number_output_nodes INT,

    created_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS model_metadata (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    preprocessing_metadata_id UUID REFERENCES preprocessing_metadata,
    model_name TEXT,
    version TEXT,
    epochs INT,
    learning_rate FLOAT,
    validation_split FLOAT,
    mae_test FLOAT,
    mae_train FLOAT,
    created_at TIMESTAMP
);
