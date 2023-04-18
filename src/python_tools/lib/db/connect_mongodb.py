import pymongo
from dotenv import find_dotenv, dotenv_values
from requests.structures import CaseInsensitiveDict


def connect_mongodb():
    config = CaseInsensitiveDict(dotenv_values(find_dotenv()))
    connection_string = config["MONGO_CONNECT"]
    client = pymongo.MongoClient(connection_string)
    try:
        client.server_info()  # validate connection string
    except pymongo.errors.ServerSelectionTimeoutError:
        raise TimeoutError("Invalid API for MongoDB connection string or timed out when attempting to connect")

    return client


if __name__ == "__main__":
    connect_mongodb()
