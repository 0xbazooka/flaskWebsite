import sqlite3
from flask import Flask



app = Flask(__name__)

#create and connect db
db = sqlite3.connect("app.db")

# create tables and cols
db.execute("CREATE TABLE users (id integer, name text, balance integer)")