import contextlib
from urllib.request import urlopen


class Query:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.query = self.make_query()

    def make_query(self):
        # create query request using self.a and self.b
        return self.query

    def make_request_and_get_response(self):  # <--- the 'dangerous' method that can raise exceptions
        with contextlib.closing(urlopen(self.query)) as response:
            return response.read().decode('utf-8')
