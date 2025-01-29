from pysnc import ServiceNowClient

# Replace these variables with your ServiceNow instance details
INSTANCE = 'your_instance_name'
USERNAME = 'your_username'
PASSWORD = 'your_password'

# Change number to search for
CHANGE_NUMBER = 'CHG0001234'

# Initialize the client
client = ServiceNowClient(INSTANCE, USERNAME, PASSWORD)

# Define the table to query
table = 'change_request'

# Define the query parameters
query = {'number': CHANGE_NUMBER}

# Perform the query
response = client.glide.get(table, query)

# Check if the response is successful
if response.status_code == 200:
    # Parse the JSON response
    result = response.json()
    if result['result']:
        change_record = result['result'][0]
        print(f"Change Record found: {change_record}")
    else:
        print("No change record found with the provided change number.")
else:
    print(f"Failed to retrieve change record. Status code: {response.status_code}")
    print(f"Error message: {response.json().get('error', {}).get('message', 'No error message available')}")

# Close the client connection
client.session.close()
