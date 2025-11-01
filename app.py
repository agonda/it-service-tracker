from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from datetime import datetime
import requests
import os

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET", "devsecretkey")

DB_PATH = 'requests.db'
DEPT_API = 'https://jsonplaceholder.typicode.com/users'

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        requester_name TEXT,
        department TEXT,
        category TEXT,
        description TEXT,
        status TEXT,
        created_at TEXT)''')
    conn.commit()
    conn.close()

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def fetch_departments():
    try:
        resp = requests.get(DEPT_API, timeout=4)
        resp.raise_for_status()
        users = resp.json()
        depts = []
        for u in users:
            if isinstance(u, dict):
                comp = u.get('company', {}).get('name')
                if comp:
                    depts.append(comp)
                else:
                    name = u.get('name')
                    if name:
                        depts.append(name)
        seen = set()
        result = []
        for d in depts:
            if d not in seen:
                seen.add(d)
                result.append(d)
        return result if result else fallback_departments()
    except Exception:
        return fallback_departments()

def fallback_departments():
    return ["Human Resources","Finance","Operations","IT","Facilities","Sales","Marketing","Customer Service"]

@app.route('/')
def index():
    conn = get_db_connection()
    rows = conn.execute("SELECT * FROM requests ORDER BY created_at DESC").fetchall()
    conn.close()
    total = len(rows)
    pending = sum(1 for r in rows if r['status'] == 'Pending')
    resolved = sum(1 for r in rows if r['status'] == 'Resolved')
    return render_template('index.html', requests=rows, total=total, pending=pending, resolved=resolved)

@app.route('/new', methods=['GET','POST'])
def new_request():
    if request.method == 'POST':
        name = request.form['name']
        dept = request.form['department']
        cat = request.form['category']
        desc = request.form['description']
        if not all([name, dept, cat, desc]):
            flash('Please fill all fields.', 'danger')
            return redirect(url_for('new_request'))
        status = 'Pending'
        created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        conn = get_db_connection()
        conn.execute("INSERT INTO requests (requester_name, department, category, description, status, created_at) VALUES (?, ?, ?, ?, ?, ?)",(name, dept, cat, desc, status, created_at))
        conn.commit(); conn.close()
        flash('Request submitted successfully. Status set to Pending.', 'success')
        return redirect(url_for('index'))
    departments = fetch_departments()
    return render_template('new.html', departments=departments)

@app.route('/resolve/<int:request_id>', methods=['POST'])
def resolve_request(request_id):
    conn = get_db_connection()
    cur = conn.execute("SELECT * FROM requests WHERE id = ?", (request_id,))
    if not cur.fetchone():
        conn.close()
        flash('Request not found.', 'danger')
        return redirect(url_for('index'))
    conn.execute("UPDATE requests SET status = 'Resolved' WHERE id = ?", (request_id,))
    conn.commit(); conn.close()
    flash(f'Request {request_id} marked as Resolved.', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
