from flask import Flask, get_flashed_messages, request, jsonify, redirect, session, render_template, flash, url_for
import sqlite3, random;
import os, sys
from time import sleep
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)

app.secret_key = os.urandom(24)



def get_database_connection():
    conn = sqlite3.connect('quotes.db')
    # conn.row_factory = sqlite3.Row
    return conn

def typewriter(words):
    for char in words:
        sleep(0.5)
        print(char)
    

@app.route('/')
def startPage():
    return render_template('startPage.html')

@app.route('/loginPage')
def loginPage():
    return render_template('login.html')

@app.route('/signupPage')
def signupPage():
    return render_template('signup.html')

@app.route('/addPage')
def addPage():
    return render_template('addQuotes.html')

@app.route('/login', methods=['POST'])
def login ():
    username = request.form['username']
    password = request.form['password']
    conn = get_database_connection()
    user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
    pas = conn.execute('SELECT * FROM users WHERE USERNAME = ? AND PASSWORD = ?', (username, password)).fetchone()
    conn.close()
    if user and pas:
        session['username'] = username 
        return redirect(url_for('generator'))  
    else:
        flash("Incorrect Username or Password")
        return redirect(url_for('loginPage'))


@app.route('/signup', methods = ['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    confirm = request.form['confirm']

    if password != confirm:
        flash("Passwords Don't Match")
        return redirect(url_for('signupPage'))
    
    conn = get_database_connection()
    existing_user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()

    if existing_user:
        flash("Username already in use")
        return redirect(url_for('signupPage'))
    
    conn = get_database_connection()
    conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()
    return redirect(url_for('generator'))




@app.route('/quotes', methods = ['GET'])
def getQuotes():
    conn = get_database_connection()
    quotes = conn.execute('SELECT * FROM quotes').fetchall()
    conn.close()
    ranQuote = random.choice(quotes)
    return render_template('main.html', quote = ranQuote[2], author = ranQuote[1])

@app.route('/addQuotes', methods = ['POST'])
def addQuote():
    quote = request.form['quote']
    author = request.form['author']
    if not quote or not author:
        flash("Empty Quote or Author")
        return redirect(url_for('addQuotes'))
    conn = get_database_connection()
    conn.execute('INSERT INTO quotes (quote, author) VALUES (?, ?)', (quote, author))
    conn.commit()
    conn.close()
    return redirect(url_for('generator'))


@app.route('/generator')
def generator():
    return render_template('main.html')


if __name__ == "__main__":
    app.run(debug=True)


#Idea: Quote Generator
#Functions:
#Generates Quotes from a given 55-ish
#Takes in Quotes to add into the list of quotes


#Requirements:
#user-id so that each user can have their own quotes







#3 GET -> Request data from a specified resource
#1 POST -> Create a resource


