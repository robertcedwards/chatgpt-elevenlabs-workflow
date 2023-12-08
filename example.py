import requests

# Function to store data to a file
def store_data(filename, data):
    with open(filename, 'w') as file:
        file.write(data)

# Function to read data from a file
def read_data(filename):
    with open(filename, 'r') as file:
        return file.read()

# Function for a hypothetical API call using the data
def make_api_call(data):
    # Replace this URL with the actual API endpoint you want to use
    api_url = "https://example.com/api"
    response = requests.post(api_url, json={'data': data})
    return response.json()

# Example usage
response_data = "This is the response from a prompt"
filename = "response_data.txt"

# Store the data
store_data(filename, response_data)

# Read the data back
stored_data = read_data(filename)

# Use the stored data for another API call
api_response = make_api_call(stored_data)

print(api_response)
