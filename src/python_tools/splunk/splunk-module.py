import splunklib.client as client
import splunklib.results as results


def search_splunk_logs(splunk_host, splunk_port, bearer_token, index, search_query):
    # Connect to Splunk
    service = client.connect(
        host=splunk_host,
        port=splunk_port,
        token=bearer_token,
    )

    # Combine the search query with the index
    full_search_query = f'search index="{index}" {search_query}'

    # Run the search
    job = service.jobs.create(full_search_query)

    # Wait for the job to complete
    while not job.is_done():
        job.refresh()

    # Retrieve the results
    result_stream = job.results(output_mode="json")
    results_reader = results.JSONResultsReader(result_stream)

    # Collect all results
    final_results = [result for result in results_reader]

    return final_results
if __name__ == "__main__":
    splunk_host = "your-splunk-server"
    splunk_port = 8089  # Default management port
    bearer_token = "your_bearer_token"
    index = "your_index"
    search_query = '"Out of Memory Error"'

    results = search_splunk_logs(splunk_host, splunk_port, bearer_token, index, search_query)
    for result in results:
        print(result)
