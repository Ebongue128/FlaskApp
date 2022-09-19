import sqlite3
from flask import Flask, render_template, session, request

def get_db_connection():
	conn = sqlite3.connect('database.db')
	conn.row_factory = sqlite3.Row
	return conn

def is_logged_in():
	try:
		return session["username"] == "VisitorProjetAWS2022"
	except:
		return False

def login():
	session['username'] = "VisitorProjetAWS2022"

def add_visitor():
	ip_address = request.remote_addr
	conn = get_db_connection()
	conn.execute("INSERT INTO visits (ip_address) VALUES (?)", (ip_address,))
	conn.commit()
	conn.close()

def page_views():
	conn = get_db_connection()
	visits = conn.execute('SELECT * FROM visits LIMIT 10').fetchall()
	nb = conn.execute("SELECT COUNT(*) FROM visits").fetchone()[0]
	conn.close()
	return visits, nb


app = Flask(__name__)

app.secret_key = b'GODisGreat'

@app.route('/')
def index():
	#if not is_logged_in():
	#	add_visitor()
	#	login()
	add_visitor()
	visits, nb = page_views()
	return render_template('index.html', visits=visits, nb = nb)

