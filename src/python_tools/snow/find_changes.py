from pysnc import ServiceNowClient
from datetime import datetime, timedelta

# Replace these variables with your ServiceNow instance details
INSTANCE = 'your_instance_name'
USERNAME = 'your_username'
PASSWORD = 'your_password'

def list_closed_changes_yesterday():
    # Initialize the client
    client = ServiceNowClient(INSTANCE, USERNAME, PASSWORD)

    # Define the table to query
    table = 'change_request'

    # Calculate yesterday's date
    yesterday = datetime.now() - timedelta(days=1)
    start_of_yesterday = yesterday.replace(hour=0, minute=0, second=0, microsecond=0)
    end_of_yesterday = yesterday.replace(hour=23, minute=59, second=59, microsecond=999999)

    # Format the dates as strings in ServiceNow's format
    start_of_yesterday_str = start_of_yesterday.strftime('%Y-%m-%d %H:%M:%S')
    end_of_yesterday_str = end_of_yesterday.strftime('%Y-%m-%d %H:%M:%S')

    # Define the query parameters
    query = {
        'closed_at>=': start_of_yesterday_str,
        'closed_at<=': end_of_yesterday_str,
        'state': 'closed'
    }

    # Perform the query
    response = client.glide.get(table, query)

    # Check if the response is successful
    if response.status_code == 200:
        # Parse the JSON response
        result = response.json()
        if result['result']:
            print(f"Change Records closed yesterday ({start_of_yesterday_str} to {end_of_yesterday_str}):")
            for change_record in result['result']:
                print(change_record)
        else:
            print("No change records closed yesterday.")
    else:
        print(f"Failed to retrieve change records. Status code: {response.status_code}")
        print(f"Error message: {response.json().get('error', {}).get('message', 'No error message available')}")

    # Close the client connection
    client.session.close()
