import sqlite3
import pandas as pd

def get_database_data(model):
    # Connect to the SQLite database
    conn = sqlite3.connect('db.sqlite3')

    # Get the name of the table associated with the model
    table_name = model._meta.db_table

    # Read data from the database into a Pandas DataFrame
    df = pd.read_sql_query("SELECT * FROM {}".format(table_name), conn)

    # Write the DataFrame to a CSV file
    # df.to_csv('data.csv', index=False)

    # Close the connection to the database
    conn.close()

    # We return the dataframe to interact with
    return df