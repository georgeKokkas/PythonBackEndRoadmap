# Send a GET request to a public API and print the response data.

# Import the 'requests' library to handle HTTP requests
import requests

# Define the URL of the public API
url = "https://jsonplaceholder.typicode.com/posts"

# Send a GET request to the specified URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the JSON content of the response
    print(response.json())
else:
    print(f"Request failed with status code {response.status_code}")
