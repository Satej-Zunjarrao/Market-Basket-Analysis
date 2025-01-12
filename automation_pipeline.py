"""
Module: automation_pipeline.py
Description: This module integrates all steps of the market basket analysis pipeline,
             automating the data extraction, preprocessing, analysis, and export processes.
Author: Satej
"""

import os
from data_extraction import extract_data
from data_preprocessing import clean_data, create_transaction_item_matrix
from eda_visualization import analyze_item_popularity, plot_item_popularity, visualize_sales_trends
from association_rule_mining import find_frequent_itemsets, generate_association_rules, save_rules_to_csv
from dashboard_export import export_to_excel

# Paths and configuration constants
DATABASE_PATH = "satej_retail_database.db"
SQL_QUERY = """
    SELECT transaction_id, item, quantity, transaction_date
    FROM transactions
"""
RAW_DATA_PATH = "satej_transaction_data.csv"
CLEANED_MATRIX_PATH = "satej_transaction_item_matrix.csv"
FREQUENT_ITEMSETS_PATH = "satej_frequent_itemsets.csv"
ASSOCIATION_RULES_PATH = "satej_association_rules.csv"
OUTPUT_VISUALS_FOLDER = "visualizations/"
OUTPUT_DASHBOARD_DATA_PATH = "satej_dashboard_data.xlsx"
MIN_SUPPORT = 0.01
MIN_CONFIDENCE = 0.2
MIN_LIFT = 1.5


def ensure_folder_exists(folder_path):
    """
    Ensures that the specified folder exists. Creates it if it doesn't.

    Parameters:
        folder_path (str): Path to the folder.

    Returns:
        None
    """
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created folder: {folder_path}")


def run_pipeline():
    """
    Executes the entire market basket analysis pipeline, integrating all steps.

    Returns:
        None
    """
    try:
        # Step 1: Data Extraction
        print("\n=== Step 1: Data Extraction ===")
        extract_data(DATABASE_PATH, SQL_QUERY, RAW_DATA_PATH)

        # Step 2: Data Preprocessing
        print("\n=== Step 2: Data Preprocessing ===")
        cleaned_data = clean_data(RAW_DATA_PATH)
        create_transaction_item_matrix(cleaned_data, CLEANED_MATRIX_PATH)

        # Step 3: Exploratory Data Analysis
        print("\n=== Step 3: Exploratory Data Analysis ===")
        ensure_folder_exists(OUTPUT_VISUALS_FOLDER)
        item_popularity = analyze_item_popularity(cleaned_data)
        plot_item_popularity(item_popularity, OUTPUT_VISUALS_FOLDER)
        visualize_sales_trends(cleaned_data, OUTPUT_VISUALS_FOLDER)

        # Step 4: Association Rule Mining
        print("\n=== Step 4: Association Rule Mining ===")
        transaction_matrix = pd.read_csv(CLEANED_MATRIX_PATH, index_col=0)
        frequent_itemsets = find_frequent_itemsets(transaction_matrix, MIN_SUPPORT)
        save_rules_to_csv(frequent_itemsets, FREQUENT_ITEMSETS_PATH)

        rules = generate_association_rules(frequent_itemsets, MIN_CONFIDENCE, MIN_LIFT)
        save_rules_to_csv(rules, ASSOCIATION_RULES_PATH)

        # Step 5: Export for Dashboard
        print("\n=== Step 5: Export for Dashboard ===")
        export_to_excel(FREQUENT_ITEMSETS_PATH, ASSOCIATION_RULES_PATH, OUTPUT_DASHBOARD_DATA_PATH)

        print("\nPipeline execution completed successfully.")

    except Exception as e:
        print(f"Error in pipeline execution: {e}")


if __name__ == "__main__":
    run_pipeline()
