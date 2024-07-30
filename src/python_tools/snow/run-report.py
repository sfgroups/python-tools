from pysnc import ServiceNowClient
import pandas as pd

# Replace these variables with your ServiceNow instance details
INSTANCE = 'your_instance_name'
USERNAME = 'your_username'
PASSWORD = 'your_password'
REPORT_SYS_ID = 'your_report_sys_id'  # The Sys ID of the pre-defined report

# Initialize the client
client = ServiceNowClient(INSTANCE, USERNAME, PASSWORD)

# URL for the ServiceNow report API
url = f'https://{INSTANCE}.service-now.com/api/now/v1/report/{REPORT_SYS_ID}/execute'

# Make the GET request to run the report
response = client.session.get(url, headers={"Accept": "application/json"})

# Check if the response is successful
if response.status_code == 200:
    # Parse the JSON response
    result = response.json()
    report_data = result.get('result', {}).get('data', [])

    # Convert the data to a pandas DataFrame
    if report_data:
        df = pd.DataFrame(report_data)
        # Save the DataFrame to an Excel file
        df.to_excel('report_output.xlsx', index=False)
        print("Report data has been saved to 'report_output.xlsx'.")
    else:
        print("No data found in the report.")
else:
    print(f"Failed to run report. Status code: {response.status_code}")
    print(f"Error message: {response.json().get('error', {}).get('message', 'No error message available')}")

# Close the client connection
client.session.close()
