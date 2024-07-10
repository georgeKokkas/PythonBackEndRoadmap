# Send a POST request to a public API with some data and print the response.

# Import the 'requests' library to handle HTTP requests
import requests

# Define the URL of the public API
url = "https://jsonplaceholder.typicode.com/posts"

# Define the data to be sent in the POST request
data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

# Send a POST request to the specified URL with the data
response = requests.post(url, json=data)

# Check if the request was successful (status code 201 for created)
if response.status_code == 201:
    # Print the JSON content of the response
    print(response.json())
else:
    print(f"Request failed with status code {response.status_code}")
