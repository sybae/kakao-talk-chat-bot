from flask import Flask, g
from flask_restful import Api
from app import message
import sqlite3

# Default Environment Setting.
app = Flask(__name__)
api = Api(app)
message.addResouceDef(api)
DATABASE = 'whatisyour.db'

# Check the DB connection.
def request_has_connection():
    return hasattr(g, 'db')

# Try to DB connect.
def connect_db():
    return g.db

# Run it before connection.
@app.before_request
def before_request():
    if not request_has_connection():
        g.db = sqlite3.connect(DATABASE)

# Run it after working.
@app.teardown_request
def teardown_request(exception):
    if request_has_connection():
        g.db.close()

# Excute SQL Query. (SELECT)
def excute_sql_select(sqlQuery, sqlParam):
    conn = connect_db()
    cur = conn.cursor()
    sqlParam = "" if sqlParam is None else sqlParam
    return cur.execute(sqlQuery, sqlParam)

# Excute SQL Query. (INSERT, UPDATE, DELETE)
def excute_sql_update(sqlQuery, sqlParam):
    conn = connect_db()
    cur = conn.cursor()

    if sqlParam is None or sqlParam == {}:
        return False

    cur.execute(sqlQuery, sqlParam)
    conn.commit()
    return True
