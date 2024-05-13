from app import app
from flask import Flask, render_template, flash, redirect, url_for
import mysql.connector
from app.forms import LoginForm


db = mysql.connector.connect(
   host="localhost",
   user="cubinez85",
   password="123",
   database="testdb"
)

cursor = db.cursor()

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'cubinez85'}
    posts = [
        {
            'author': {'username': 'Иван'},
            'body': {'Как дела?'}
        },
        {
            'author': {'username': 'Серж'},
            'body': {'ok'}
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/tables')
def tables():

    cursor.execute(
"select * from user join post"

)
    content = cursor.fetchall()
    cursor.execute(
"select * from user join post"

)
    labels = cursor.fetchall()
    labels = list(map(lambda x: x[0], cursor.description))

    return render_template('testdb.html', labels=labels, content=content)

@app.route('/admin')
def admin():

    cursor.execute(
"select u.username, p.body, p.timestamp from user u join post p where u.id=1"

)
    content = cursor.fetchall()
    cursor.execute(
"select u.username, p.body, p.timestamp from user u join post p where u.id=1"

)
    labels = cursor.fetchall()
    labels = list(map(lambda x: x[0], cursor.description))

    return render_template('testdb.html', labels=labels, content=content)
