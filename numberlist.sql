--start code here

--pull in dataset to sql

CREATE TABLE IF NOT EXISTS mock_data (
    id INTEGER PRIMARY KEY,
    DIDs TEXT,
    DIDs Available TEXT,
    DIDs Used TEXT,
    Description TEXT,
    reserve TEXT
);