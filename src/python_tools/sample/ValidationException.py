class SD3ValidationException(Exception):
    def __init__(self, error_code, source, details):
        super().__init__(f"Error Code: {error_code}, Source: {source}, Details: {details}")
        self.error_code = error_code
        self.source = source
        self.details = details

    def __str__(self):
        return f"SD3ValidationException({self.error_code}): {self.details} [Source: {self.source}]"

# Example usage:
try:
    raise SD3ValidationException(404, "Database", "Data not found in the database")
except SD3ValidationException as e:
    print(e)
