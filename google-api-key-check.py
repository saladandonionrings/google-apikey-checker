import requests
import sys
from termcolor import colored

def test_google_maps_api(api_key):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address=Paris&key={api_key}"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200 and data['status'] == 'OK' and data['results']:
        formatted_address = data['results'][0]['formatted_address']
        location = data['results'][0]['geometry']['location']
        output = f"API Key is valid. Response:\nAddress: {formatted_address}\nLocation: Latitude {location['lat']}, Longitude {location['lng']}"
        print(colored(output, 'green'))
    elif data['status'] == 'REQUEST_DENIED':
        error_message = "API Key is invalid."
        print(colored(error_message, 'red'))
    else:
        error_message = "The request did not return any results."
        print(colored(error_message, 'yellow')) 

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: google-api-tester.py <api_key>")
    else:
        api_key = sys.argv[1]
        test_google_maps_api(api_key)
