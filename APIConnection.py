import requests

url = "https://site.api.espn.com/apis/site/v2/sports/basketball/nba/players"

# Send a GET request to the API
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the response data (in JSON format)
    print(response.json())
else:
    # Print an error message if the request was not successful
    print(f"Error: {response.status_code} - {response.text}")