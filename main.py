#!/usr/bin/python3

import flask #install version: 0.12.2
import os

from flask import Flask 
from flask import render_template
from functools import wraps
from flask import request, Response, session, flash

app = Flask(__name__)

#https://pythonspot.com/en/login-authentication-with-flask/
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('mainsite.html')
    else:
        return "Hello Boss!"
 
@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()

"""
def check_auth(username, password):
    """"""This function is called to check if a username /
    password combination is valid.""""""
    return username == 'admin' and password == 'secret'

@app.route("/")
def hello():
    #return "Hello World!"
    return render_template("mainsite.html")

@app.route("/login", methods=['POST'])
def login():
	username=request.form['username']
	password=request.form['password']
	if check_auth(username, password):
		return render_template("appsite.html")
	else:
		return redirect('/')
#http://flask.pocoo.org/docs/0.12/tutorial/


@app.route("/send", methods=['POST'])
def sentMessage():
	username=request.form['username']
	message=request.form['message']

	print(username)
	print(message)
	return "dfsfdsfsd"#render_template("appsite.html")
"""

if __name__ == "__main__":
	app.secret_key = os.urandom(12)
	print("MyProgram started running")
	app.run(host="127.0.0.1", port=4000)
