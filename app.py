from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from forms import RegisterForm, LoginForm

import logging

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


        # Insert the new user into the database
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (username, password, email, balance) VALUES (?, ?, ?, ?)",
                  (username, password, email, 0))
        conn.commit()
        conn.close()

        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)


# Route for logging in
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        # print(f'Email: {form.email.data}')
        # print(f'Password: {form.password.data}')
        def check_password(password, user_password):
            return password == user_password

        # Connect to the SQLite database
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # Query the database for the entered username
        cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
        user = cursor.fetchone()
        if user and check_password(user[3], password):
            # Login is successful, redirect to the home page
            print(user)
            print(check_password(user[3], password))
            return redirect(url_for('home'))
        else:
            # If the login fails, redirect the user to the login page or show an error message
            return redirect(url_for('register'))
    else:
        return render_template('login.html', form=form)



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)