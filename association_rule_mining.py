"""
Module: association_rule_mining.py
Description: This module applies the Apriori algorithm to find frequent itemsets and 
             generates association rules using confidence and lift metrics.
Author: Satej
"""

import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Constants for input and output file paths
INPUT_MATRIX_PATH = "satej_transaction_item_matrix.csv"  # Path to the transaction-item matrix
OUTPUT_RULES_PATH = "satej_association_rules.csv"  # Path to save the association rules


def find_frequent_itemsets(transaction_matrix, min_support):
    """
    Identifies frequent itemsets using the Apriori algorithm.

    Parameters:
        transaction_matrix (pd.DataFrame): Binary transaction-item matrix.
        min_support (float): Minimum support threshold for frequent itemsets.

    Returns:
        pd.DataFrame: Frequent itemsets with their support values.
    """
    print("Finding frequent itemsets...")
    frequent_itemsets = apriori(transaction_matrix, min_support=min_support, use_colnames=True)
    print(f"Identified {len(frequent_itemsets)} frequent itemsets.")
    return frequent_itemsets


def generate_association_rules(frequent_itemsets, min_confidence, min_lift):
    """
    Generates association rules from frequent itemsets.

    Parameters:
        frequent_itemsets (pd.DataFrame): Frequent itemsets with support values.
        min_confidence (float): Minimum confidence threshold for rules.
        min_lift (float): Minimum lift threshold for rules.

    Returns:
        pd.DataFrame: Association rules with confidence and lift metrics.
    """
    print("Generating association rules...")
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence)
    rules = rules[rules['lift'] >= min_lift]
    print(f"Generated {len(rules)} association rules.")
    return rules


def save_rules_to_csv(rules, output_path):
    """
    Saves the generated association rules to a CSV file.

    Parameters:
        rules (pd.DataFrame): Association rules DataFrame.
        output_path (str): Path to save the CSV file.

    Returns:
        None
    """
    print(f"Saving association rules to {output_path}...")
    rules.to_csv(output_path, index=False)
    print("Association rules saved successfully.")


if __name__ == "__main__":
    # Load the transaction-item matrix
    print(f"Loading transaction-item matrix from {INPUT_MATRIX_PATH}...")
    transaction_matrix = pd.read_csv(INPUT_MATRIX_PATH, index_col=0)

    # Set thresholds
    MIN_SUPPORT = 0.01  # Minimum support threshold
    MIN_CONFIDENCE = 0.2  # Minimum confidence threshold
    MIN_LIFT = 1.5  # Minimum lift threshold

    # Perform association rule mining
    frequent_itemsets = find_frequent_itemsets(transaction_matrix, MIN_SUPPORT)
    rules = generate_association_rules(frequent_itemsets, MIN_CONFIDENCE, MIN_LIFT)

    # Save the association rules
    save_rules_to_csv(rules, OUTPUT_RULES_PATH)
