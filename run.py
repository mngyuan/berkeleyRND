import sqlite3
from contextlib import closing

from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

# g is application globals: flask.g can have any application global
# stored on it. we will store db connection info.

import config

# startup
# this will also load config.py down the line
from rndapp import app


#DB FUNCTIONALITY
def connect_db():
    return sqlite3.connect(app.config(['DATABASE']))

# initializes the db, as in deletes everything
# and makes bare tables
def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

# END DB STUFF

# REQUEST SETUP AND TEARDOWN
@app.before_request
def before_request():
	g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
	db = getattr(g, 'db', None)
	if db is not None:
		# db was connected. let's disconnect
		db.close()

# Login management

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(uid):
	# returns None on invalid user
	return User.get(userid)


app.run(debug = config.DEBUG)