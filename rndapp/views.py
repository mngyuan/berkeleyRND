# what each page will look like

from rndapp import app
from flask import render_template, flash, redirect, request
from login import LoginForm

from config import ANALYTICS
app.config['ANALYTICS'] = ANALYTICS #wait is this neccessary

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
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        # TODO: this constructor call is fake; update when User has a real constructor
        user = User(form.loginuname.data, form.email.data, form.password.data)
        db_session.add(user)
        flash('Thank you for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    loginform = LoginForm()
    if loginform.validate_on_submit():
        # flash('Login requested for OpenID="' + loginform.openid.data + '", remember_me=' + str(loginform.remember_me.data))
        # return redirect('/index')
        login_user(user)
        flash("Logged in successfully.")
        return redirect(request.args.get("next") or url_for("home")
    return render_template("login.html", form=loginform)

    # return render_template("login.html",
    #     title="Log in", form=loginform,
    #     providers = app.config['OPENID_PROVIDERS'])

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))

@app.route('/settings')
@login_required
def settings():
    pass