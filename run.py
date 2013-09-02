import sqlite3
from contextlib import closing

from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

import config

# startup
# this will also load config.py down the line
from rndapp import app

def connect_db():
    return sqlite3.connect(app.config(['DATABASE']))

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

app.run(debug = config.DEBUG)