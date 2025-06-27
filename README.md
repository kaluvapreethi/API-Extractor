# API-Extractor
# Random Activity API Extractor

This project demonstrates a simple data extraction pipeline that fetches random activity suggestions from the [Bored API](https://www.boredapi.com/api/activity), processes the data, and saves it into both JSON and CSV formats.

## Features

* **API Integration:** Fetches data from a public REST API.
* **JSON Parsing:** Handles and extracts information from JSON responses.
* **Error Handling:** Implements basic error handling for network issues, HTTP errors, and JSON decoding problems.
* **Data Serialization:** Saves raw API responses as timestamped JSON files.
* **Data Transformation (Basic):** Extracts specific fields from the JSON and appends them to a structured CSV file.
* **File Management:** Organizes output files in a dedicated `data/` directory.

## Technologies Used

* **Python 3.x**
* **`requests` library:** For making HTTP requests to the API.
* **`json` module:** For working with JSON data.
* **`csv` module:** For writing data to CSV files.
* **`os` and `datetime` modules:** For file path management and timestamping.

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/](https://github.com/)<YourUsername>/random-activity-api-extractor.git
    cd random-activity-api-extractor
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## How to Run

After setting up, simply run the main Python script:

```bash
python api_extractor.py