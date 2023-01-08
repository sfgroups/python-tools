import urllib

from python_tools.pytest_samples.query import Query

def get_response_from_external_api(query):
    try:
        response = query.make_request_and_get_response()
    except urllib.error.URLError as e:
        print('Got a URLError: ', e)
    except urllib.error.HTTPError as e:
        print('Got a HTTPError: ', e)



if __name__ == "__main__":
    query = Query('input A', 'input B')
    result = get_response_from_external_api(query)
    print(result)
