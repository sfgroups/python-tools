from sqlalchemy import text

# Create the table with unique constraints if it doesn't exist
df.head(0).to_sql('users', con=engine, if_exists='append', index=False)

# Insert or replace records using PostgreSQL's ON CONFLICT clause
insert_query = """
INSERT INTO users (id, name, age)
VALUES (:id, :name, :age)
ON CONFLICT(id) DO UPDATE SET
name = EXCLUDED.name,
age = EXCLUDED.age;
"""

with engine.connect() as connection:
    for _, row in df.iterrows():
        connection.execute(text(insert_query), **row)
