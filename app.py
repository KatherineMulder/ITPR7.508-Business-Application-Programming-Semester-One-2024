from flask import Flask, render_template, request, redirect, url_for, session
import psycopg2
from mortgage import Mortgage
import plotly.graph_objs as go

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
                session['username'] = username
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
        try:
            with psycopg2.connect(
                    dbname="mortgage_calculator",
                    user="postgres",
                    password="admin123",
                    host="localhost",
                    port="5432") as conn:

                conn.autocommit = True

                with conn.cursor() as cursor:
                    cursor.execute("SELECT * FROM mortgages")
                    mortgages = cursor.fetchall()

                    mortgage_details = [(mortgage[0], mortgage[1], mortgage[2], mortgage[3], mortgage[4], mortgage[5],
                                         mortgage[6], mortgage[7], mortgage[8], mortgage[9], mortgage[10], mortgage[11],
                                         mortgage[12])
                                        for mortgage in mortgages]

                    interests = [mortgage[10] for mortgage in mortgages]
                    principals = [mortgage[11] for mortgage in mortgages]
                    mortgage_names = [mortgage[1] for mortgage in mortgages]

                    chart_html = generate_interest_principal_chart(interests, principals, mortgage_names)

        except psycopg2.Error as e:
            error_message = "Error fetching data from database: {}".format(e)
            app.logger.error(error_message)
            return render_template("index.html", error_message=error_message)

        username = session['username']
        return render_template("index.html", username=username, mortgages=mortgages, mortgage_details=mortgage_details,
                               chart_html=chart_html)
    else:
        return redirect(url_for("login"))


@app.route('/new_mortgage', methods=['GET', 'POST'])
def new_mortgage():
    if request.method == 'POST':
        mortgage_name = request.form['mortgage_name']
        principal = float(request.form['initial_principal'])
        interest = float(request.form['initial_interest'])
        term_years = int(request.form['initial_term'])
        deposit = float(request.form.get('deposit', 0))
        extra_costs = float(request.form.get('extra_costs', 0))

        new_mortgage = Mortgage(
            mortgage_id=None,
            mortgage_name=mortgage_name,
            start_date=None,
            initial_interest=interest,
            initial_term=term_years,
            initial_principal=principal,
            deposit=deposit,
            extra_costs=extra_costs
        )

        monthly_interest = round(new_mortgage.calculate_monthly_interest(), 2)
        monthly_repayment = round(new_mortgage.calculate_monthly_repayment(), 2)
        monthly_principal_repayment = round(new_mortgage.calculate_monthly_principal_repayment(), 2)
        fortnightly_interest = round(new_mortgage.calculate_fortnightly_interest(), 2)
        fortnightly_repayment = round(new_mortgage.calculate_fortnightly_repayment(), 2)
        fortnightly_principal_repayment = round(new_mortgage.calculate_fortnightly_principal_repayment(), 2)

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
            INSERT INTO mortgages (mortgage_name, principal, interest, term_years, deposit, extra_costs,
                                   monthly_interest, monthly_repayment, monthly_principal_repayment,
                                   fortnightly_interest, fortnightly_repayment, fortnightly_principal_repayment)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
                       (mortgage_name, principal, interest, term_years, deposit, extra_costs,
                        monthly_interest, monthly_repayment, monthly_principal_repayment,
                        fortnightly_interest, fortnightly_repayment, fortnightly_principal_repayment))

        conn.close()

        return redirect(url_for('index'))

    return render_template('new_mortgage.html')


def generate_interest_principal_chart(interests, principals, mortgage_names):
    data = [
        go.Scatter(x=mortgage_names, y=interests, mode='lines+markers', name='Interest'),
        go.Scatter(x=mortgage_names, y=principals, mode='lines+markers', name='Principal')
    ]
    layout = go.Layout(title='Interest and Principal Payments')
    fig = go.Figure(data=data, layout=layout)
    return fig.to_html(full_html=False)


@app.route("/update_mortgage")
def update_mortgage():
    return render_template("update_mortgage.html")


@app.route("/remove_mortgage")
def remove_mortgage():
    return render_template("remove_mortgage.html")



@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))



if __name__ == "__main__":
    app.run(debug=True)
