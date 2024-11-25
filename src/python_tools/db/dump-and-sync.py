import psycopg2
from psycopg2.extras import execute_batch


def get_connection(host, database, user, password, port=5432):
    """
    Establish a connection to a PostgreSQL database.
    """
    return psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        port=port
    )


def dump_and_sync_data(source_conn, target_conn, table_name, primary_key):
    """
    Dump data from a source table and sync it to a target table.
    Performs an UPSERT operation (INSERT or UPDATE based on primary key).
    """
    try:
        source_cursor = source_conn.cursor()
        target_cursor = target_conn.cursor()

        # Fetch data from the source table
        source_cursor.execute(f"SELECT * FROM {table_name}")
        rows = source_cursor.fetchall()
        column_names = [desc[0] for desc in source_cursor.description]

        # Build the INSERT query with ON CONFLICT for UPSERT
        placeholders = ", ".join(["%s"] * len(column_names))
        columns = ", ".join(column_names)
        update_columns = ", ".join([f"{col} = EXCLUDED.{col}" for col in column_names if col != primary_key])
        upsert_query = f"""
            INSERT INTO {table_name} ({columns})
            VALUES ({placeholders})
            ON CONFLICT ({primary_key}) DO UPDATE
            SET {update_columns}
        """

        # Sync data to the target table
        execute_batch(target_cursor, upsert_query, rows)
        target_conn.commit()

        print(f"Data successfully synced for table: {table_name}")

    except Exception as e:
        target_conn.rollback()
        print(f"Error syncing data for table {table_name}: {e}")
    finally:
        source_cursor.close()
        target_cursor.close()


def sync_multiple_tables(source_config, target_config, tables_info):
    """
    Sync multiple tables between source and target databases.

    :param source_config: Dict containing source DB connection details.
    :param target_config: Dict containing target DB connection details.
    :param tables_info: List of dictionaries with table names and primary keys.
                        Example: [{'table_name': 'table1', 'primary_key': 'id'}, ...]
    """
    source_conn = get_connection(**source_config)
    target_conn = get_connection(**target_config)

    try:
        for table_info in tables_info:
            table_name = table_info["table_name"]
            primary_key = table_info["primary_key"]
            dump_and_sync_data(source_conn, target_conn, table_name, primary_key)
    finally:
        source_conn.close()
        target_conn.close()


if __name__ == "__main__":
    # Source database configuration
    source_db_config = {
        "host": "source_host",
        "database": "source_db",
        "user": "source_user",
        "password": "source_password",
        "port": 5432
    }

    # Target database configuration
    target_db_config = {
        "host": "target_host",
        "database": "target_db",
        "user": "target_user",
        "password": "target_password",
        "port": 5432
    }

    # Tables to sync with primary keys
    tables_to_sync = [
        {"table_name": "table1", "primary_key": "id"},
        {"table_name": "table2", "primary_key": "id"},
        # Add more tables as needed
    ]

    # Sync data
    sync_multiple_tables(source_db_config, target_db_config, tables_to_sync)
