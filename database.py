import psycopg2


def create_database():
    # Connect to the default database (e.g., "postgres")
    default_conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="admin123",
        host="localhost",
        port="5432"
    )
    default_conn.autocommit = True
    default_cursor = default_conn.cursor()

    # Check if the database "mortgage_calculator" exists
    default_cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'mortgage_calculator'")
    database_exists = default_cursor.fetchone()

    if not database_exists:
        # Create the database "mortgage_calculator" if it doesn't exist
        default_cursor.execute("CREATE DATABASE mortgage_calculator")

    default_conn.close()

    # Connect to the newly created database "mortgage_calculator"
    conn = psycopg2.connect(
        dbname="mortgage_calculator",
        user="postgres",
        password="admin123",
        host="localhost",
        port="5432"
    )
    conn.autocommit = True
    cursor = conn.cursor()

    # Create the "users" table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            userid SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(50) NOT NULL
        )
    """)

    # Insert sample data into the "users" table
    users = [
        (12345678, 'kat', 'password'),
        (87654321, 'alex', 'password1'),
        (56781234, 'john', 'password2')
    ]
    cursor.executemany("INSERT INTO users (userid, username, password) VALUES (%s, %s, %s)", users)

    conn.commit()
    conn.close()


create_database()
