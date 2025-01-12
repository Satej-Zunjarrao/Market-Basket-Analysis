"""
Module: dashboard_export.py
Description: This module exports processed data (frequent itemsets and association rules)
             to a format compatible with Power BI or Tableau for dashboard creation.
Author: Satej
"""

import pandas as pd

# Constants for input and output paths
FREQUENT_ITEMSETS_PATH = "satej_frequent_itemsets.csv"  # Path to the frequent itemsets file
ASSOCIATION_RULES_PATH = "satej_association_rules.csv"  # Path to the association rules file
OUTPUT_DASHBOARD_DATA_PATH = "satej_dashboard_data.xlsx"  # Path to save dashboard-compatible data


def export_to_excel(frequent_itemsets_path, association_rules_path, output_path):
    """
    Exports frequent itemsets and association rules to an Excel file for use in dashboards.

    Parameters:
        frequent_itemsets_path (str): Path to the CSV file containing frequent itemsets.
        association_rules_path (str): Path to the CSV file containing association rules.
        output_path (str): Path to save the combined Excel file.

    Returns:
        None
    """
    try:
        # Load frequent itemsets and association rules from CSV files
        print("Loading frequent itemsets...")
        frequent_itemsets = pd.read_csv(frequent_itemsets_path)
        print("Loading association rules...")
        association_rules = pd.read_csv(association_rules_path)

        # Save data to an Excel file with separate sheets
        print(f"Exporting data to {output_path}...")
        with pd.ExcelWriter(output_path, engine="xlsxwriter") as writer:
            frequent_itemsets.to_excel(writer, sheet_name="Frequent Itemsets", index=False)
            association_rules.to_excel(writer, sheet_name="Association Rules", index=False)

        print("Data export completed successfully.")

    except Exception as e:
        print(f"Error during export: {e}")


if __name__ == "__main__":
    # Export processed data for dashboard visualization
    export_to_excel(FREQUENT_ITEMSETS_PATH, ASSOCIATION_RULES_PATH, OUTPUT_DASHBOARD_DATA_PATH)
