# what each page will look like

from rndapp import app
from flask import render_template, flash, redirect, request
# from forms import LoginForm

from config import ANALYTICS
app.config['ANALYTICS'] = ANALYTICS

from random import choice

@app.route('/')
@app.route('/home') # PUT THIS DOWN AT INDEX WHEN ROLLING OUT
# normally would go with route /home,
# but let's make a placeholder page.

def comingsoon():
    return render_template("comingsoon.html")

@app.route('/notyet')
def index():
    #placeholder vars
    user = {'nickname': 'Kevin'}
    posts = [
        {
            'author': {'nickname': 'Miguel'},
            'body': 'Beautiful day in Berkeley!'
        },
        {
            'author': {'nickname': 'Wilshire'},
            'body': 'Should I buy a new guitar?'
        }
    ]
    
    return render_template("index.html",
        title="Home",
        user = user,
        posts = posts)

@app.route('/about')
def about():
    return render_template("about.html")
@app.route('/projects')
def about():
    return render_template("projects.html")

@app.errorhandler(404)
def page_not_found(e):
    msgs = ['Oops!', 'Doh!', 'Oh no!', 'Aw shucks.', 'Golly.', 'Damn']
    return render_template("404.html", 
        msg=choice(msgs)), 404

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     loginform = LoginForm()
#     if loginform.validate_on_submit():
#         flash('Login requested for OpenID="' + loginform.openid.data + '", remember_me=' + str(loginform.remember_me.data))
#         return redirect('/index')

#     return render_template("login.html",
#         title="Log in", form=loginform,
#         providers = app.config['OPENID_PROVIDERS'])
    