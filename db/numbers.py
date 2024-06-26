import pandas as pd
import sqlite3

# Replace 'input.csv' with your CSV file path
csv_file = 'MOCK_DATA.csv'
# Replace 'output.db' with your desired SQLite database file path
db_file = 'MOCK_DATA.db'
# Replace 'table_name' with the name you want for your SQLite table
table_name = 'numbers'

# Load CSV into a pandas DataFrame
df = pd.read_csv(csv_file)

# Establish SQLite connection and write DataFrame to SQLite
conn = sqlite3.connect(db_file)
df.to_sql(table_name, conn, if_exists='replace', index=False)

# Commit changes and close the connection
conn.commit()
conn.close()

print(f'CSV file "{csv_file}" successfully imported into SQLite database "{db_file}" as table "{table_name}"')
