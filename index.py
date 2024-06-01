import csv
import requests

def check_url_status(url):
    try:
        with requests.head(url, stream=True) as response:
            return response.status_code
    except requests.RequestException:
        return -1

input_file = 'urls.csv'
output_file = '404_urls.csv'

def display_title():
    print("\U0001F6A8  404 URL Checker  \U0001F6A8")

# Display title
display_title()

try:
    with open(input_file, mode='r', newline='') as file, open(output_file, 'a', newline='') as csvfile:
        csv_reader = csv.reader(file)
        csv_writer = csv.writer(csvfile)

        for row in csv_reader:
            if len(row) >= 0:
                file_url = (col.strip() for col in row)
                status_code = check_url_status(file_url)
                status_message = "Not Found" if status_code == 404 else "OK"
                print(f"\U0001F310 {file_url} - Status: {status_message}")
                if status_code == 404:
                    csv_writer.writerow([file_url])

except Exception as e:
    print("\U0001F6AB Error occurred while processing the URLs. Please check the file.")
    print(f"Error: {e}")
