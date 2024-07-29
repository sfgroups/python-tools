import pytest
from datetime import datetime, timedelta

from python_tools.snow.find_changes import list_closed_changes_yesterday # Import your function

@pytest.fixture
def mock_servicenow_client(mocker):
    # Mock the ServiceNowClient and its methods
    mock_client = mocker.Mock()
    mock_get = mocker.Mock()
    mock_client.glide.get = mock_get
    mocker.patch('python_tools.snow.find_changes.ServiceNowClient', return_value=mock_client)
    return mock_client

def test_list_closed_changes_yesterday(mock_servicenow_client, mocker):
    # Prepare the mock response data
    yesterday = datetime.now() - timedelta(days=1)
    start_of_yesterday = yesterday.replace(hour=0, minute=0, second=0, microsecond=0)
    end_of_yesterday = yesterday.replace(hour=23, minute=59, second=59, microsecond=999999)
    start_of_yesterday_str = start_of_yesterday.strftime('%Y-%m-%d %H:%M:%S')
    end_of_yesterday_str = end_of_yesterday.strftime('%Y-%m-%d %H:%M:%S')

    mock_response_data = {
        "result": [
            {"number": "CHG0001234", "closed_at": start_of_yesterday_str, "state": "closed"},
            {"number": "CHG0005678", "closed_at": end_of_yesterday_str, "state": "closed"}
        ]
    }
    mock_servicenow_client.glide.get.return_value.status_code = 200
    mock_servicenow_client.glide.get.return_value.json.return_value = mock_response_data

    # Call the function to test
    list_closed_changes_yesterday()

    # Assert that the glide.get method was called with the correct query parameters
    expected_query = {
        'closed_at>=': start_of_yesterday_str,
        'closed_at<=': end_of_yesterday_str,
        'state': 'closed'
    }
    mock_servicenow_client.glide.get.assert_called_once_with('change_request', expected_query)

    # Check the output (you may want to capture and assert output if your function prints results)
