# what each page will look like

from rndapp import app, db
from flask import render_template, flash, redirect, request, g, url_for
from forms import LoginForm, RegistrationForm
from random import choice
from models import User

from flask.ext.login import login_required, login_user, \
    logout_user, fresh_login_required

@app.route('/')
@app.route('/home') # PUT THIS DOWN AT INDEX WHEN ROLLING OUT
# normally would go with route /home,
# but let's make a placeholder page.

def comingsoon():
    return render_template("comingsoon.html",
        surpress_rcontent=True)

#@app.route('/notyet')
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
        posts = posts,
        surpress_rcontent=True)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/projects')
def projects():
    return render_template("projects.html")

@app.route('/events')
def events():
    return render_template("events.html")

@app.route('/news')
def news():
    return render_template("news.html")


@app.errorhandler(404)
def page_not_found(e):
    msgs = ['Oops!', 'Doh!', 'Oh no!', 'Aw shucks.', 'Golly.', 'Damn']
    return render_template("404.html", 
        msg=choice(msgs)), 404


    

# user specific pages
#@app.route('/register', methods=['GET', 'POST'])
def register():
    regform = RegistrationForm(request.form)
    if request.method == 'POST' and regform.validate():
        user = User(regform.loginuname.data, regform.password.data, \
            regform.firstname.data, regform.lastname.data, regform.email.data)
        g.user = user
        # add to db
        db.session.add(user)
        db.session.commit()

        flash('Thank you for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=regform)

#@app.route('/login', methods=['GET', 'POST'])
def login():
    loginform = LoginForm()
    if request.method == 'POST' and loginform.validate():
        # flash('Login requested for OpenID="' + loginform.openid.data + '", remember_me=' + str(loginform.remember_me.data))
        # return redirect('/index')
        login_user(user)
        flash("Logged in successfully.")
        return redirect(request.args.get("next") or url_for("home"))
    return render_template("login.html", form=loginform)

    # return render_template("login.html",
    #     title="Log in", form=loginform,
    #     providers = app.config['OPENID_PROVIDERS'])

#@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))

#@app.route('/settings')
@fresh_login_required
def settings():
    pass
