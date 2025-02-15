""" Demo Python Flask Application """

import os
import sys

import psycopg2

from flask import Flask, render_template, redirect

# Connect to the database
db = 'host=10.17.50.126 dbname=test_0 user=test_0 password=test'
conn = psycopg2.connect(db)
cur = conn.cursor()

app = Flask(__name__)


@app.route("/")
def root():
    cur.execute(
    """
        SELECT * FROM badges 
        ORDER BY random()
        LIMIT 25 
    """)
    rows = cur.fetchall()

    return render_template("base.html", rows=rows)


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
