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


def closed_change():
    from pysnc import ServiceNowClient
    from datetime import datetime, timedelta

    # ServiceNow credentials and instance details
    INSTANCE = "your_instance_name"
    USER = "your_username"
    PASSWORD = "your_password"

    # Connect to the ServiceNow instance
    client = ServiceNowClient(INSTANCE, USER, PASSWORD)

    # Calculate the date range for the last week
    today = datetime.utcnow()
    last_week = today - timedelta(days=7)

    # Convert dates to the format required by ServiceNow
    today_str = today.strftime('%Y-%m-%d %H:%M:%S')
    last_week_str = last_week.strftime('%Y-%m-%d %H:%M:%S')

    # Query to get the "closed" change records in the last week
    gr = client.GlideRecord('change_request')
    gr.addQuery('sys_updated_on', '>=', last_week_str)
    gr.addQuery('sys_updated_on', '<=', today_str)
    gr.addQuery('state', '=', 'closed')  # Assuming "closed" state is represented as 'closed'
    gr.query()

    # Print the results
    while gr.hasNext():
        record = gr.next()
        sys_id = record.sys_id
        number = record.number
        closed_at = record.sys_updated_on
        print(f"Change ID: {sys_id}, Number: {number}, Closed At: {closed_at}")


def closed_changes2():
    import requests
    from datetime import datetime, timedelta

    # ServiceNow credentials and instance details
    INSTANCE = "your_instance_name"
    USER = "your_username"
    PASSWORD = "your_password"

    # ServiceNow API URL
    url = f"https://{INSTANCE}.service-now.com/api/sn_chg_rest/change"

    # Calculate the date range for the last week
    today = datetime.utcnow()
    last_week = today - timedelta(days=7)

    # Convert dates to the format required by ServiceNow
    today_str = today.strftime('%Y-%m-%dT%H:%M:%S')
    last_week_str = last_week.strftime('%Y-%m-%dT%H:%M:%S')

    # Define the query parameters
    params = {
        'sysparm_query': f'sys_updated_onBETWEEN{last_week_str}@{today_str}^state=closed',
        'sysparm_limit': '100'  # Limit the number of results
    }

    # Send the GET request
    response = requests.get(url, auth=(USER, PASSWORD), params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()  # Parse the JSON response
        for record in data['result']:
            sys_id = record.get('sys_id')
            number = record.get('number')
            closed_at = record.get('sys_updated_on')
            print(f"Change ID: {sys_id}, Number: {number}, Closed At: {closed_at}")
    else:
        print(f"Failed to retrieve data: {response.status_code}, {response.text}")
