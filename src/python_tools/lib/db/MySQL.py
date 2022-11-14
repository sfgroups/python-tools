from dotenv import find_dotenv, dotenv_values
from mysql.connector import MySQLConnection
from requests.structures import CaseInsensitiveDict
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL


def get_connection():
    config = CaseInsensitiveDict(dotenv_values(find_dotenv()))

    # keep only these kes
    needed_keys = ['host', 'port', 'database', 'user', 'password']
    filtered_d = dict((k.lower(), config[k]) for k in needed_keys if k in config)
    conn = MySQLConnection(**filtered_d)
    return conn


def get_engine_kwargs():
    config = CaseInsensitiveDict(dotenv_values(find_dotenv()))
    # keep only these kes
    needed_keys = ['host', 'port', 'database', 'user', 'password', 'username']
    db_url = dict((k.lower(), config[k]) for k in needed_keys if k in config)
    db_url['drivername'] = 'mysql+pymysql'
    if 'user' in db_url:
        db_url['username'] = db_url['user']
        db_url.pop('user')
    engine = create_engine(URL.create(**db_url), echo=False, future=True)
    return engine


def get_engine():
    return get_engine_kwargs()


if __name__ == "__main__":
    var=10
    print(f"{var = }")
    x = get_engine_kwargs()
    print(x)