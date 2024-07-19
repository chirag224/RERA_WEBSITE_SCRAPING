# Project Details Scraper

This project contains a Python script that scrapes project details such as GSTIN No, PAN No, Name, and Permanent Address from the HPRERA website. The scraped data is then saved into a CSV file named `project_details.csv`.

## Table of Contents

- [Project Details Scraper](#project-details-scraper)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [File Descriptions](#file-descriptions)
  - [Dependencies](#dependencies)
  - [License](#license)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/project-details-scraper.git
    cd project-details-scraper
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Ensure you have ChromeDriver installed and its path added to your system's PATH. You can download ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).

2. Run the script:

    ```bash
    python main.py
    ```

3. The script will scrape the project details from the HPRERA website and save them into `project_details.csv` in the current directory.

## File Descriptions

- `main.py`: The main script that performs the web scraping and saves the data to a CSV file.
- `requirements.txt`: Contains the list of dependencies required to run the script.
- `project_csv`: Directory where the CSV file `project_details.csv` will be saved.

## Dependencies

The script requires the following Python packages:

- selenium
- csv

You can install these dependencies using the command:

```bash
pip install -r requirements.txt
