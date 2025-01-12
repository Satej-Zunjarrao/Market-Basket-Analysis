"""
Module: data_extraction.py
Description: This module is responsible for extracting transactional data from a SQL database 
             and saving it in a CSV format for further analysis.
Author: Satej
"""

import pandas as pd
import sqlite3

# Constants for database connection and output file
DATABASE_PATH = "satej_retail_database.db"  # Path to the retail database
SQL_QUERY = """
    SELECT transaction_id, item, quantity, transaction_date
    FROM transactions
"""
OUTPUT_CSV_PATH = "satej_transaction_data.csv"  # Path to save extracted data


def extract_data(database_path, sql_query, output_csv_path):
    """
    Extracts transactional data from the specified database and saves it as a CSV file.
    
    Parameters:
        database_path (str): Path to the SQLite database file.
        sql_query (str): SQL query to fetch data from the database.
        output_csv_path (str): Path to save the extracted data as a CSV file.

    Returns:
        None
    """
    try:
        # Establish a connection to the SQLite database
        print("Connecting to database...")
        connection = sqlite3.connect(database_path)

        # Execute the SQL query and fetch data into a Pandas DataFrame
        print("Executing SQL query...")
        data = pd.read_sql_query(sql_query, connection)

        # Save the extracted data to a CSV file
        print(f"Saving data to {output_csv_path}...")
        data.to_csv(output_csv_path, index=False)

        print("Data extraction completed successfully.")

    except Exception as e:
        print(f"Error during data extraction: {e}")
    finally:
        # Close the database connection
        connection.close()
        print("Database connection closed.")


if __name__ == "__main__":
    # Execute data extraction process
    extract_data(DATABASE_PATH, SQL_QUERY, OUTPUT_CSV_PATH)
