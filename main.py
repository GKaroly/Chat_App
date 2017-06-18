#!/usr/bin/python3

import flask #install version: 0.12.2
import os
import datetime

from flask import Flask 
from flask import render_template
from functools import wraps
from flask import request, Response, session, flash, g , redirect, url_for

app = Flask(__name__)

#based on this site:
#https://github.com/PrettyPrinted/flask-sessions/blob/master/session.py
#And these youtube videos:
#https://www.youtube.com/watch?v=T1ZVyY1LWOg
#https://www.youtube.com/watch?v=eBwhBrNbrNI&index=3&list=PLXmMXHVSvS-CMpHUeyIeqzs3kl-tIG-8R

#https://pythonspot.com/en/login-authentication-with-flask/
"""@app.route('/')
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

messages=[]
users={
    "users": [{
        "username": "admin",
        "password": "secret"
    }, {
        "username": "test",
        "password": "password"
    }]
}


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid."""

    for user in users["users"]:
        if username == user["username"] and password == user["password"]:
            return True

    return False
"""
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



"""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session.pop('user', None)

        username=request.form['username']
        password=request.form['password']

        if check_auth(username, password):
            session['user'] = username
            #what is url_for
            return redirect(url_for('protected'))

    return render_template('mainsite.html')

@app.route('/protected')
def protected():
    if g.user:

        StringToShow=""
        for element in messages[-10:]:
            TempMessage=str(element["date"])+" - "+element["user"]+": \n"
            TempMessage+=str(element["message"]+"\n")
            StringToShow+=TempMessage
        return render_template('appsite.html', signedUsername=g.user, channelContent=StringToShow)

    return redirect(url_for('index'))

@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

@app.route('/getsession')
def getsession():
    if 'user' in session:
        return session['user']

    return 'Not logged in!'

@app.route('/dropsession')
def dropsession():
    session.pop('user', None)
    return 'Dropped!'


#Other methods
@app.route("/send", methods=['POST'])
def sentMessage():
    username=session['user']
    message=request.form['message']

    print(username)
    print(message)

    newMessage={}
    newMessage["date"]=datetime.datetime.now()
    newMessage["user"]=username
    newMessage["message"]=message

    messages.append(newMessage)
    #dropsession()
    return redirect("/protected")

@app.route("/refresh", methods=['GET'])
def refresh():
    return redirect("/protected")

if __name__ == "__main__":
    
    app.secret_key = os.urandom(12)
    print("MyProgram started running")
    app.run(host="127.0.0.1", port=4000)
