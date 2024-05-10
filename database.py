import psycopg2


def create_database():
    default_conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="admin123",
        host="localhost",
        port="5432"
    )
    default_conn.autocommit = True
    default_cursor = default_conn.cursor()

    # check database exists
    default_cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'mortgage_calculator'")
    database_exists = default_cursor.fetchone()

    if not database_exists:
        default_cursor.execute("CREATE DATABASE mortgage_calculator")

    default_conn.close()

    # connect to the newly created database mortgage_calculator
    conn = psycopg2.connect(
        dbname="mortgage_calculator",
        user="postgres",
        password="admin123",
        host="localhost",
        port="5432"
    )
    conn.autocommit = True
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            userid SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(50) NOT NULL
        )
    """)

    users = [
        ('kat', 'password'),
        ('alex', 'password1'),
        ('john', 'password2')
    ]

    # Insert users only if they don't already exist
    for user in users:
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", user)
        except psycopg2.IntegrityError:
            # User already exists, skip insertion
            continue

    conn.commit()
    conn.close()


create_database()
