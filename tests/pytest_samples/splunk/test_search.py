import requests
import time
import json


def search_splunk_logs(splunk_host, bearer_token, index, search_query):
    # Headers with the Bearer token for authentication
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    # Search endpoint
    search_endpoint = f"{splunk_host}/services/search/jobs"

    # Data for the search job
    search_data = {
        "search": search_query,
        "output_mode": "json"
    }

    # Create a search job
    search_response = requests.post(search_endpoint, headers=headers, data=search_data)
    search_response.raise_for_status()

    # Get the search job ID
    search_job_id = search_response.json()["sid"]

    # Check the search job status until it's done
    search_results_endpoint = f"{splunk_host}/services/search/jobs/{search_job_id}/results"

    while True:
        # Query for search job status
        job_status_response = requests.get(f"{splunk_host}/services/search/jobs/{search_job_id}", headers=headers)
        job_status_response.raise_for_status()

        job_status = job_status_response.json()
        if job_status["entry"][0]["content"]["isDone"]:
            break
        time.sleep(2)

    # Retrieve the search results
    results_response = requests.get(search_results_endpoint, headers=headers)
    results_response.raise_for_status()

    # Parse and return the results
    results = results_response.json()
    return results