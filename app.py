from flask import Flask, flash, redirect, render_template, request, session
from helpers.decorations import *
import sys
import os


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/protected')
@login_required
def protected():
    flash('You loggedin!!')
    return render_template('protected.html')

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        if request.form['password'] == '123' and request.form['username'] == 'admin':
            session['logged_in'] = True
            return redirect('/protected')
        else:
            flash('wrong password!')
    else:
        return render_template('login.html')

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect('/')

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, port=7000)
