"""
Module: utils.py
Description: This module contains helper functions such as logging, folder management, 
             and error handling, used throughout the project.
Author: Satej
"""

import os
import logging


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
        logging.info(f"Created folder: {folder_path}")
    else:
        logging.info(f"Folder already exists: {folder_path}")


def setup_logging(log_file_path="pipeline.log"):
    """
    Sets up logging for the project, directing logs to a file.

    Parameters:
        log_file_path (str): Path to save the log file.

    Returns:
        None
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file_path),
            logging.StreamHandler()
        ]
    )
    logging.info("Logging initialized.")


def log_exception(e):
    """
    Logs an exception with detailed information.

    Parameters:
        e (Exception): The exception to log.

    Returns:
        None
    """
    logging.error(f"Exception occurred: {e}", exc_info=True)


if __name__ == "__main__":
    # Example usage of the utility functions
    setup_logging()
    try:
        ensure_folder_exists("example_folder")
    except Exception as e:
        log_exception(e)
