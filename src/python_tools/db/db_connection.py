import os
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_connection_url():
    # Get the user's home directory
    home_dir = Path.home()

    # Create the path to the 'temp' folder in the home directory
    temp_dir = home_dir / "temp"

    # Create the 'temp' folder if it doesn't exist
    if not temp_dir.exists():
        temp_dir.mkdir(parents=True)

    # Define the SQLite database file path
    db_file = temp_dir / "test.db"

    # Return the SQLite URL for SQLAlchemy
    sqlite_url = f"sqlite:///{db_file}"

    return sqlite_url


def get_sqlalchemy_engine():
    """
    Return an SQLAlchemy engine using the SQLite URL.
    """
    sqlite_url = get_connection_url()

    # Create an SQLAlchemy engine using the SQLite URL
    engine = create_engine(sqlite_url, echo=False)  # `echo=True` for SQL query logging
    return engine


def get_db():
    session_local = sessionmaker(bind=get_sqlalchemy_engine(), autoflush=False, autocommit=False, expire_on_commit=True)
    return session_local()


# Example usage
if __name__ == "__main__":
    db_url = get_connection_url()
    print(f"SQLite URL: {db_url}")

    engine = get_sqlalchemy_engine()
    print(f"SQLAlchemy Engine: {engine}")
