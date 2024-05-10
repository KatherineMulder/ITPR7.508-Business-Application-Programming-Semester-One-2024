from flask import Flask, render_template, request, redirect, url_for, session
import psycopg2

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret key"


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


@app.route("/", methods=["GET", "POST"])
def root():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
            user = cursor.fetchone()

            cursor.close()
            conn.close()

            if user:
                session['username'] = username  # Setting the username in session
                return redirect(url_for("index"))
            else:
                return redirect(url_for("signup"))

        except Exception as e:
            return f"An error occurred: {str(e)}"

    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if password != confirm_password:
            return render_template("signup.html", error="Passwords do not match")

        try:
            conn = connect_to_database()
            cursor = conn.cursor()

            cursor.execute("SELECT 1 FROM users WHERE username = %s", (username,))
            existing_user = cursor.fetchone()

            if existing_user:
                return render_template("signup.html", error="Username already exists")

            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            conn.commit()

            cursor.close()
            conn.close()

            return redirect(url_for("index"))

        except Exception as e:
            return f"An error occurred: {str(e)}"

    return render_template("signup.html")


@app.route("/index")
def index():
    if 'username' in session:
        username = session['username']
        return render_template("index.html", username=username)
    else:
        return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
