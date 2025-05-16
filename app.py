from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET'])
def serve_form():
    return render_template("index.html")

@app.route('/grievance', methods=['POST'])
def handle_grievance():
    name = request.form['name']
    title = request.form['title']
    message = request.form['message']
    mood = request.form['mood']
    severity = request.form['severity']

    conn = sqlite3.connect('grievances.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS grievances 
              (name TEXT, title TEXT, message TEXT, mood TEXT, severity TEXT)""")
    c.execute("""INSERT INTO grievances (name, title, message, mood, severity) 
              VALUES (?, ?, ?, ?, ?)""",
              (name, title, message, mood, severity))
    conn.commit()
    conn.close()

    return redirect(url_for('serve_form', success='true'))

@app.route('/list')  # Add this new route
def list_grievances():
    conn = sqlite3.connect('grievances.db')
    c = conn.cursor()
    c.execute("SELECT * FROM grievances")
    grievances = c.fetchall()
    conn.close()
    return render_template("list.html", grievances=grievances)

if __name__ == '__main__':
    app.run(port=5000)