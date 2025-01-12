"""
Module: constants.py
Description: This module contains constants used across the project, such as file paths,
             database connection strings, and algorithm parameters.
Author: Satej
"""

# File Paths
DATABASE_PATH = "satej_retail_database.db"  # Path to the retail database
RAW_DATA_PATH = "satej_transaction_data.csv"  # Path to save the raw transactional data
CLEANED_MATRIX_PATH = "satej_transaction_item_matrix.csv"  # Path to save the processed transaction-item matrix
FREQUENT_ITEMSETS_PATH = "satej_frequent_itemsets.csv"  # Path to save the frequent itemsets
ASSOCIATION_RULES_PATH = "satej_association_rules.csv"  # Path to save the association rules
OUTPUT_VISUALS_FOLDER = "visualizations/"  # Folder to save visualizations
OUTPUT_DASHBOARD_DATA_PATH = "satej_dashboard_data.xlsx"  # Path to save dashboard-compatible data

# SQL Query
SQL_QUERY = """
    SELECT transaction_id, item, quantity, transaction_date
    FROM transactions
"""

# Algorithm Parameters
MIN_SUPPORT = 0.01  # Minimum support threshold for frequent itemsets
MIN_CONFIDENCE = 0.2  # Minimum confidence threshold for association rules
MIN_LIFT = 1.5  # Minimum lift threshold for association rules
