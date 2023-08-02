from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from forms import RegisterForm, LoginForm

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


app.config['SECRET_KEY'] = '011d552f9bf6c46ba8b7379603e3c0b3'

# Route for registering a new user
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # Get form data
        username = form.username.data
        email = form.email.data
        password = form.password.data

        # Hash the password
        hashed_password = generate_password_hash(password)

        # Insert the new user into the database
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (user_name, password, email, balance) VALUES (?, ?, ?, ?)",
                  (username, hashed_password, email, 0))
        conn.commit()
        conn.close()

        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)


# Route for logging in
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Check if user exists in the database and password is correct
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        username = form.username.data
        password = form.password.data

        c.execute("SELECT * FROM users WHERE user_name = ?", (username,))
        user = c.fetchone()

        if user and check_password_hash(user[2], password):
            # User exists and password is correct, log them in
            user_obj = User(user[0], user[1], user[2])
            login_user(user_obj)
            flash('Logged in successfully.')
            return redirect(url_for('home'))
        else:
            # User does not exist or password is incorrect
            flash('Invalid username or password.')

    return render_template('login.html', title='Login', form=form)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)