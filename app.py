from flask import Flask, render_template, request
import sqlite3
from datetime import datetime
import os

from flask import jsonify

app = Flask(__name__)
DB_NAME = 'grievances.db'

def init_db():
    if not os.path.exists(DB_NAME):
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE grievances (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    title TEXT NOT NULL,
                    grievance TEXT NOT NULL,
                    mood TEXT,
                    severity TEXT,
                    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
        print("Database initialized.")

@app.route('/')
def grievance_form():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name, title, grievance, mood, severity, submitted_at FROM grievances ORDER BY submitted_at DESC")
        all_grievances = cursor.fetchall()
    return render_template('form.html', submitted=False, grievances=all_grievances)

@app.route('/submit', methods=['POST'])
def submit_grievance():
    name = request.form['name']
    title = request.form['title']
    grievance = request.form['grievance']
    mood = request.form['mood']
    severity = request.form['severity']

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO grievances (name, title, grievance, mood, severity)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, title, grievance, mood, severity))
        conn.commit()

        cursor.execute("SELECT name, title, grievance, mood, severity, submitted_at FROM grievances ORDER BY submitted_at DESC")
        all_grievances = cursor.fetchall()

    return render_template('form.html', submitted=True, grievances=all_grievances)


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
