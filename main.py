#!/usr/bin/python3

import flask #install version: 0.12.2

from flask import Flask 
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    #return "Hello World!"
    return render_template("mainsite.html")

#http://flask.pocoo.org/docs/0.12/tutorial/

if __name__ == "__main__":
	print("MyProgram")
	app.run()
