404 URL Checker
Overview

This Python script checks a list of URLs from a CSV file and identifies the URLs returning a 404 status code. It writes the details of the 404 URLs to another CSV file for further analysis.
Setup
    Clone the Repository:

    git clone https://github.com/piyushpathar/404-url-checker.git


Navigate to the Repository:

    cd 404-url-checker


Install Requirements:

    pip install -r requirements.txt

Usage
  Prepare Input CSV File:
        Create a CSV file named urls.csv.
        List the URLs to check in the CSV file.
  Run the Script:

    python3 404_url_checker.py

 View Output:
        Check the 404_urls.csv file for URLs returning a 404 status code.

Notes

    Ensure the URLs in the input CSV file are correctly formatted.
    Review the output CSV file for URLs returning a 404 status code.

