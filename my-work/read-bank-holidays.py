# This script reads bank holiday data from a public API and prints the first event for Northern Ireland.
# Author: Carmine Giardino

import requests
url =" https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()
print(data)
northern_ireland_key ="northern-ireland"
print(f"The first {northern_ireland_key} event is: {data[northern_ireland_key]['events'][0]}")