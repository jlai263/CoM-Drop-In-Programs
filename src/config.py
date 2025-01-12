"""
src/config.py

Centralized configuration constants for the project.
"""

# Example: Replace this with the actual request URL used in your browser’s Network tab
EVENTS_URL = (
    "https://anc.ca.apm.activecommunities.com/activemississauga/rest/onlinecalendar/multicenter/events?locale=en-US"
    # add query parameters if needed
)

DATA_DIR = "../data"
RAW_HTML_DIR = f"{DATA_DIR}/raw_html"
CSV_OUTPUT_FILE = f"{DATA_DIR}/events.csv"
