# what each page will look like

from rndapp import app
from flask import render_template, flash, redirect
# from forms import LoginForm


@app.route('/')
@app.route('/index')
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

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     loginform = LoginForm()
#     if loginform.validate_on_submit():
#         flash('Login requested for OpenID="' + loginform.openid.data + '", remember_me=' + str(loginform.remember_me.data))
#         return redirect('/index')

#     return render_template("login.html",
#         title="Log in", form=loginform,
#         providers = app.config['OPENID_PROVIDERS'])
    