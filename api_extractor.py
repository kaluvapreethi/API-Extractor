{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import requests\
import json\
import csv\
import os\
from datetime import datetime\
\
# --- Configuration ---\
API_URL = "https://www.boredapi.com/api/activity"\
OUTPUT_DIR = "data"\
JSON_FILENAME_PREFIX = "activity_data"\
CSV_FILENAME_PREFIX = "activity_summary"\
\
def fetch_activity_data(url: str) -> dict or None:\
    """\
    Fetches data from the specified API URL.\
\
    Args:\
        url (str): The API endpoint URL.\
\
    Returns:\
        dict or None: A dictionary containing the API response data if successful,\
                      otherwise None.\
    """\
    print(f"Attempting to fetch data from: \{url\}")\
    try:\
        response = requests.get(url, timeout=10)\
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)\
        return response.json()\
    except requests.exceptions.HTTPError as http_err:\
        print(f"HTTP error occurred: \{http_err\} (Status Code: \{response.status_code\})")\
    except requests.exceptions.ConnectionError as conn_err:\
        print(f"Connection error occurred: \{conn_err\}. Check your internet connection.")\
    except requests.exceptions.Timeout as timeout_err:\
        print(f"Timeout error occurred: \{timeout_err\}. The request took too long.")\
    except requests.exceptions.RequestException as req_err:\
        print(f"An unexpected error occurred during the request: \{req_err\}")\
    except json.JSONDecodeError as json_err:\
        print(f"Failed to decode JSON from response: \{json_err\}. Response text: \{response.text\}")\
    return None\
\
def save_to_json(data: dict, filename: str) -> None:\
    """\
    Saves the given dictionary data to a JSON file.\
\
    Args:\
        data (dict): The dictionary to save.\
        filename (str): The full path for the output JSON file.\
    """\
    try:\
        with open(filename, 'w', encoding='utf-8') as f:\
            json.dump(data, f, indent=4, ensure_ascii=False)\
        print(f"Data successfully saved to JSON: \{filename\}")\
    except IOError as e:\
        print(f"Error saving JSON file \{filename\}: \{e\}")\
\
def save_to_csv(data: dict, filename: str) -> None:\
    """\
    Extracts specific fields from the activity data and saves them to a CSV file.\
\
    Args:\
        data (dict): The activity data dictionary.\
        filename (str): The full path for the output CSV file.\
    """\
    # Define the fields you want to save to CSV\
    # The order here determines the column order in the CSV\
    fieldnames = ['activity', 'type', 'participants', 'price', 'accessibility', 'link', 'key']\
\
    # Ensure all fieldnames exist in the data dictionary to avoid KeyError\
    # Provide a default value (e.g., None or empty string) if a key is missing\
    row_data = \{field: data.get(field) for field in fieldnames\}\
\
    # Check if the file already exists to decide whether to write headers\
    file_exists = os.path.exists(filename)\
\
    try:\
        with open(filename, 'a', newline='', encoding='utf-8') as f: # 'a' for append mode\
            writer = csv.DictWriter(f, fieldnames=fieldnames)\
\
            if not file_exists or os.stat(filename).st_size == 0: # Write header only if file is new or empty\
                writer.writeheader()\
            \
            writer.writerow(row_data)\
        print(f"Data successfully appended to CSV: \{filename\}")\
    except IOError as e:\
        print(f"Error saving CSV file \{filename\}: \{e\}")\
\
def main():\
    """\
    Main function to run the API extraction and data saving process.\
    """\
    # Create output directory if it doesn't exist\
    if not os.path.exists(OUTPUT_DIR):\
        os.makedirs(OUTPUT_DIR)\
        print(f"Created output directory: \{OUTPUT_DIR\}")\
\
    activity_data = fetch_activity_data(API_URL)\
\
    if activity_data:\
        print("\\n--- Fetched Activity ---")\
        for key, value in activity_data.items():\
            print(f"\{key.capitalize()\}: \{value\}")\
\
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")\
\
        # Save to JSON\
        json_output_path = os.path.join(OUTPUT_DIR, f"\{JSON_FILENAME_PREFIX\}_\{timestamp\}.json")\
        save_to_json(activity_data, json_output_path)\
\
        # Save to CSV (appends to a single CSV file)\
        csv_output_path = os.path.join(OUTPUT_DIR, f"\{CSV_FILENAME_PREFIX\}.csv")\
        save_to_csv(activity_data, csv_output_path)\
    else:\
        print("Failed to fetch activity data. Exiting.")\
\
if __name__ == "__main__":\
    main()}