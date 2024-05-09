from flask import Flask, render_template
import psycopg2

app = Flask(__name__)


def connect_to_database():
    conn = psycopg2.connect(
        dbname="mortgage_calculator",
        user="postgres",
        password="admin123",
        host="localhost",
        port="5432"
    )
    conn.autocommit = True
    return conn


@app.route("/")
def main():
    try:
        conn = connect_to_database()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()

        cursor.close()
        conn.close()

        return render_template("login.html", users=users)
    except Exception as e:
        # Handle database errors gracefully
        return f"An error occurred: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)
