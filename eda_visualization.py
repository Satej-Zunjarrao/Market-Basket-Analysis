"""
Module: eda_visualization.py
Description: This module performs Exploratory Data Analysis (EDA) on the transactional data 
             and visualizes insights using Matplotlib and Seaborn.
Author: Satej
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Constants for input file path and output folder for visualizations
INPUT_CSV_PATH = "satej_transaction_data.csv"  # Path to the raw transactional data
OUTPUT_VISUALS_FOLDER = "visualizations/"  # Folder to save the visualizations


def analyze_item_popularity(data):
    """
    Analyzes item popularity by calculating the total number of times each item was sold.

    Parameters:
        data (pd.DataFrame): Transactional data.

    Returns:
        pd.Series: Item popularity sorted by frequency.
    """
    print("Analyzing item popularity...")
    item_popularity = data['item'].value_counts()
    return item_popularity


def plot_item_popularity(item_popularity, output_folder):
    """
    Creates and saves a bar chart for the most popular items.

    Parameters:
        item_popularity (pd.Series): Item popularity data.
        output_folder (str): Path to save the visualization.

    Returns:
        None
    """
    print("Plotting item popularity...")
    plt.figure(figsize=(10, 6))
    item_popularity.head(10).plot(kind='bar', color='skyblue')
    plt.title("Top 10 Most Popular Items", fontsize=16)
    plt.xlabel("Items", fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{output_folder}top_10_items.png")
    print("Item popularity plot saved as 'top_10_items.png'.")


def visualize_sales_trends(data, output_folder):
    """
    Creates and saves a line chart for sales trends over time.

    Parameters:
        data (pd.DataFrame): Transactional data.
        output_folder (str): Path to save the visualization.

    Returns:
        None
    """
    print("Visualizing sales trends...")
    data['transaction_date'] = pd.to_datetime(data['transaction_date'])
    sales_trends = data.groupby(data['transaction_date'].dt.date)['quantity'].sum()

    plt.figure(figsize=(12, 6))
    sales_trends.plot(kind='line', marker='o', color='orange')
    plt.title("Daily Sales Trends", fontsize=16)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Quantity Sold", fontsize=12)
    plt.grid()
    plt.tight_layout()
    plt.savefig(f"{output_folder}daily_sales_trends.png")
    print("Sales trends plot saved as 'daily_sales_trends.png'.")


if __name__ == "__main__":
    # Load the transactional data
    print(f"Loading data from {INPUT_CSV_PATH}...")
    data = pd.read_csv(INPUT_CSV_PATH)

    # Perform EDA and save visualizations
    item_popularity = analyze_item_popularity(data)
    plot_item_popularity(item_popularity, OUTPUT_VISUALS_FOLDER)
    visualize_sales_trends(data, OUTPUT_VISUALS_FOLDER)
