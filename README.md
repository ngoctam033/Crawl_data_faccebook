# Facebook Group Scraper

This project is a Python-based web scraper that extracts member information from Facebook groups. It uses Selenium WebDriver for browser automation and BeautifulSoup for parsing HTML.

## Features

- Login to Facebook
- Navigate to specified Facebook groups
- Scroll through the member list of each group
- Extract member information (name and profile link)
- Open member profiles in new tabs to check for recent activity
- Write valid member information to a CSV file

## Requirements

- Python 3.6+
- Selenium WebDriver
- BeautifulSoup
- Firefox browser
- geckodriver

## Setup

1. Clone this repository to your local machine.
2. Install the required Python packages using pip:

```bash
pip install -r requirements.txt

## Project Structure

The project has the following file structure:

```
web-scraping-project
├── src
│   ├── main.py
│   ├── scraper.py
│   └── parser.py
├── data
├── requirements.txt
└── README.md
```

- `src/main.py`: This file serves as the entry point of the project. It contains the main code to run the web scraping process.

- `src/scraper.py`: This file contains the implementation of the web scraper. It utilizes the BeautifulSoup library to parse HTML and extract data from websites.

- `src/parser.py`: This file contains helper functions or classes for parsing and manipulating the scraped data.

- `data/`: This directory is used to store any data files generated or used by the web scraping process.

## Getting Started

To set up the project, follow these steps:

1. Clone the repository or download the project files.

2. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

   This will install the necessary libraries, including BeautifulSoup.

3. Customize the `scraper.py` file to specify the websites you want to scrape and the data you want to extract.

4. Run the `main.py` file to start the web scraping process:

   ```
   python src/main.py
   ```

   The scraped data will be saved in the `data/` directory.

## Dependencies

The project requires the following dependencies:

- BeautifulSoup: A library for parsing HTML and XML documents.

You can install all the dependencies by running the command mentioned in step 2 of the "Getting Started" section.

Feel free to explore and modify the project according to your needs. Happy web scraping!