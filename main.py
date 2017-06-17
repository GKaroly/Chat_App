#!/usr/bin/python3

import flask #install version: 0.12.2

from flask import Flask 
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    #return "Hello World!"
    return render_template("mainsite.html")

@app.route("/login", methods=['POST'])
def login():
	return "Szia2"
#http://flask.pocoo.org/docs/0.12/tutorial/

if __name__ == "__main__":
	print("MyProgram started running")
	app.run(host="127.0.0.1", port=4000)
