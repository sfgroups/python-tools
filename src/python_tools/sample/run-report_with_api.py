import requests
from requests.auth import HTTPBasicAuth

# Replace these variables with your ServiceNow instance details
INSTANCE = 'your_instance_name'
USERNAME = 'your_username'
PASSWORD = 'your_password'
REPORT_SYS_ID = 'your_report_sys_id'  # The Sys ID of the pre-defined report

# URL for the ServiceNow report API
url = f'https://{INSTANCE}.service-now.com/api/now/v1/report/{REPORT_SYS_ID}/execute'

# Make the GET request to run the report
response = requests.get(url, auth=HTTPBasicAuth(USERNAME, PASSWORD), headers={"Accept": "application/json"})

# Check if the response is successful
if response.status_code == 200:
    # Parse the JSON response
    result = response.json()
    report_data = result.get('result', {})
    print("Report Data:")
    print(report_data)
else:
    print(f"Failed to run report. Status code: {response.status_code}")
    print(f"Error message: {response.json().get('error', {}).get('message', 'No error message available')}")

