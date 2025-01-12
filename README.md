# Market Basket Analysis

## Overview
The **Market Basket Analysis** project is designed to uncover associations between frequently purchased items in retail transactions. By leveraging **Association Rule Mining**, this Python-based solution provides actionable insights to optimize cross-selling strategies, product placement, and promotional activities.

This project includes a modular pipeline for:
- Data extraction
- Preprocessing
- Exploratory analysis
- Association rule mining
- Visualization
- Automation

---

## Key Features
- **Data Collection**: Extracts transactional data from SQL databases and stores it in CSV format.
- **Data Cleaning**: Structures data into a transaction-item matrix for analysis.
- **Exploratory Data Analysis (EDA)**: Visualizes item frequency and sales trends.
- **Association Rule Mining**: Identifies frequent itemsets and generates association rules using Apriori.
- **Visualization**: Provides itemset heatmaps and sales trend analysis.
- **Dashboard Export**: Prepares data for visualization in Power BI and Tableau.
- **Automation**: Automates the pipeline to refresh insights with new data periodically.

##Directory Structure
```
project/
│
├── data_extraction.py          # Extracts transactional data from the SQL database
├── data_preprocessing.py       # Cleans and processes data into a transaction-item matrix
├── eda_visualization.py        # Generates visualizations for exploratory data analysis
├── association_rule_mining.py  # Applies Apriori to generate frequent itemsets and rules
├── dashboard_export.py         # Exports processed data for Power BI/Tableau dashboards
├── automation_pipeline.py      # Orchestrates the entire Market Basket Analysis workflow
├── constants.py                # Stores reusable constants such as paths and parameters
├── utils.py                    # Provides helper functions for logging and folder management
├── README.md                   # Project documentation
```

## Modules

### 1. `data_extraction.py`
- Extracts transactional data from SQL databases using queries.
- Saves the extracted data in CSV format for further analysis.

### 2. `data_preprocessing.py`
- Cleans the raw transactional data (removing duplicates, handling missing values).
- Transforms data into a binary transaction-item matrix required for association rule mining.

### 3. `eda_visualization.py`
- Visualizes item popularity and daily sales trends.
- Saves insights as PNG images for reporting and stakeholder review.

### 4. `association_rule_mining.py`
- Uses the Apriori algorithm to identify frequent itemsets based on minimum support.
- Generates association rules with confidence and lift metrics.

### 5. `dashboard_export.py`
- Exports frequent itemsets and association rules into an Excel file.
- Creates separate sheets for use in Power BI or Tableau dashboards.

### 6. `automation_pipeline.py`
- Integrates all modules into an automated workflow.
- Ensures seamless execution of data extraction, preprocessing, analysis, and export tasks.

### 7. `constants.py`
- Centralized file for reusable paths, SQL queries, and algorithm parameters.
- Enables easy configuration and updates.

### 8. `utils.py`
- Provides helper functions for:
  - Logging progress and exceptions.
  - Ensuring required folders exist.
  - Handling miscellaneous tasks like parameter validation.

---

## Contact

For queries or collaboration, feel free to reach out:

- **Name**: Satej Zunjarrao  
- **Email**: zsatej1028@gmail.com
