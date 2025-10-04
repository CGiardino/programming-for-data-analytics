# This script reads bank holiday data from a public API and:
# 1. prints the bank holidays for Northern Ireland
# 2. prints all bank holidays for Northern Ireland that are unique to Northern Ireland (i.e. not shared with other divisions)

# Author: Carmine Giardino

import requests
bank_holidays_url = " https://www.gov.uk/bank-holidays.json"
# Get bank holiday data from the API endpoint (ref: https://www.w3schools.com/python/ref_requests_get.asp)
response_bank_holidays_api = requests.get(bank_holidays_url)
# Check if the request was successful
if response_bank_holidays_api.status_code != 200:
    print(f"Error: Unable to fetch data from the API. Status code: {response_bank_holidays_api.status_code}")
    # Exit the script with a non-zero status to indicate an error
    exit(1)
# Parse the JSON response
bank_holiday_data = response_bank_holidays_api.json()
# Get the events for Northern Ireland
northern_ireland_events = bank_holiday_data["northern-ireland"]['events']
# Extract just the dates of the events for Northern Ireland
northern_ireland_events_dates = [event['date'] for event in northern_ireland_events]
# Print the bank holidays for Northern Ireland
print(f"The Northern Ireland bank holidays are: {northern_ireland_events_dates}")

# Find all event dates across all divisions to identify unique dates. 
# Items are extracted in a nested list comprehension (ref https://www.w3schools.com/python/python_lists_comprehension.asp) 
# The nested list works as follows: first we extract divisions in bank_holiday_data.values(); then for events in division['events']; then for dates in [event['date']]
all_event_dates = [date for division in bank_holiday_data.values() for event in division['events'] for date in [event['date']]]
# Find unique Northern Ireland event dates
unique_northern_ireland_event_dates = [
    date for date in northern_ireland_events_dates 
    if all_event_dates.count(date) == 1 # date appears only once in all_event_dates
]
# Print all bank holidays for Northern Ireland that are unique to Northern Ireland (i.e. not shared with other divisions)
print(f"The unique Northern Ireland bank holidays are: {unique_northern_ireland_event_dates}")