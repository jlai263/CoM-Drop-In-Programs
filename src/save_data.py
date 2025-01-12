"""
src/save_data.py

Contains functions to save the parsed event data into CSV or other formats.
"""

import csv
import os
from src.config import CSV_OUTPUT_FILE

def save_events_to_csv(events, csv_file=CSV_OUTPUT_FILE):
    """
    Save a list of event dicts to a CSV file.
    """
    if not events:
        print("No events to save.")
        return

    # Define the columns you want in the CSV
    fieldnames = [
        "center_id",
        "center_name",
        "title",
        "start_time",
        "end_time",
        "description",
        "facility_name"
    ]

    # Ensure the directory exists
    data_dir = os.path.dirname(csv_file)
    if data_dir and not os.path.exists(data_dir):
        os.makedirs(data_dir, exist_ok=True)

    with open(csv_file, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(events)

    print(f"Events saved to {csv_file}")
