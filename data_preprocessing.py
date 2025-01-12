"""
Module: data_preprocessing.py
Description: This module handles data cleaning and transforms transactional data into a binary 
             transaction-item matrix required for association rule mining.
Author: Satej
"""

import pandas as pd

# Constants for input and output file paths
INPUT_CSV_PATH = "satej_transaction_data.csv"  # Path to the raw transactional data
OUTPUT_MATRIX_PATH = "satej_transaction_item_matrix.csv"  # Path to save the processed transaction-item matrix


def clean_data(input_csv_path):
    """
    Cleans the raw transactional data, handling missing values and duplicates.
    
    Parameters:
        input_csv_path (str): Path to the raw transactional data CSV file.

    Returns:
        pd.DataFrame: Cleaned transactional data.
    """
    try:
        # Load the raw data into a DataFrame
        print(f"Loading data from {input_csv_path}...")
        data = pd.read_csv(input_csv_path)

        # Drop duplicates if any
        print("Removing duplicate rows...")
        data.drop_duplicates(inplace=True)

        # Drop rows with missing values
        print("Dropping rows with missing values...")
        data.dropna(inplace=True)

        print("Data cleaning completed.")
        return data

    except Exception as e:
        print(f"Error during data cleaning: {e}")
        return None


def create_transaction_item_matrix(cleaned_data, output_matrix_path):
    """
    Transforms cleaned transactional data into a binary transaction-item matrix.

    Parameters:
        cleaned_data (pd.DataFrame): Cleaned transactional data.
        output_matrix_path (str): Path to save the transaction-item matrix.

    Returns:
        None
    """
    try:
        # Pivot the data to create a transaction-item matrix
        print("Creating transaction-item matrix...")
        transaction_item_matrix = (
            cleaned_data.groupby(['transaction_id', 'item'])['quantity']
            .sum()
            .unstack(fill_value=0)
            .applymap(lambda x: 1 if x > 0 else 0)  # Convert quantities to binary values
        )

        # Save the transaction-item matrix to a CSV file
        print(f"Saving transaction-item matrix to {output_matrix_path}...")
        transaction_item_matrix.to_csv(output_matrix_path)

        print("Transaction-item matrix creation completed successfully.")

    except Exception as e:
        print(f"Error during transaction-item matrix creation: {e}")


if __name__ == "__main__":
    # Execute the data preprocessing pipeline
    cleaned_data = clean_data(INPUT_CSV_PATH)
    if cleaned_data is not None:
        create_transaction_item_matrix(cleaned_data, OUTPUT_MATRIX_PATH)
