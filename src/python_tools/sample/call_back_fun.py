import sqlite3


# Function to create a database table
from pathlib import Path

from python_tools.lib.utils import utils


def create_table():
    connection = sqlite3.connect("../data/my_database.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS my_table (id INTEGER PRIMARY KEY, name TEXT)")
    connection.commit()
    connection.close()


# Function to update the database table using a callback
def update_table(callback):
    connection = sqlite3.connect("my_database.db")
    cursor = connection.cursor()

    # Get data from the callback function
    data = callback()

    for item in data:
        cursor.execute("INSERT INTO my_table (name) VALUES (?)", (item,))

    connection.commit()
    connection.close()


# Callback function to provide data for the update
def callback_function():
    data = ["John", "Alice", "Bob"]
    return data


if __name__ == "__main__":
    create_table()
    update_table(callback_function)
    print("Database table updated.")
