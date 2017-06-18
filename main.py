#!/usr/bin/python3

import flask #install version: 0.12.2

from flask import Flask 
from flask import render_template
from functools import wraps
from flask import request, Response

app = Flask(__name__)

def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
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


if __name__ == "__main__":
	print("MyProgram started running")
	app.run(host="127.0.0.1", port=4000)
