from flask import abort, Blueprint, flash, jsonify, Markup, redirect, render_template, request, url_for
from flask.ext.login import current_user, login_required

from .forms import ProjectForm
from .models import Project
from rndapp.data import query_to_list

import config

application = Blueprint("application", __name__)
application.config = config.ANALYTICS

#@application.route("/")
#@application.route("/home")
#def index():
#    return render_template("index.html")

@application.route("/")
@application.route("/home")
def index():
    return render_template("comingsoon.html", surpress_rcontent=True)

@application.route('/about')
def about():
    return render_template("about.html")

@application.route('/events')
def events():
    return render_template("events.html")

@application.route('/news')
def news():
    return render_template("news.html")

@application.errorhandler(404)
def page_not_found(e):
    msgs = ['Oops!', 'Doh!', 'Oh no!', 'Aw shucks.', 'Golly.', 'Damn']
    return render_template("404.html", 
        msg=choice(msgs)), 404

@application.route("/projects", methods=("GET", "POST"))
@login_required
def view_projects():
    form = ProjectForm()

    if form.validate_on_submit():
        Project.create(owner=current_user, **form.data)
        flash("Added project")
        return redirect(url_for(".view_projects"))

    #query = Project.query.filter(Project.user_id == current_user.id)
    query = Project.query
    data = query_to_list(query)
    results = []

    try:
        results = [next(data)]
        for row in data:
            row = [_make_link(cell) if i == 0 else cell
                   for i, cell in enumerate(row)]
            results.append(row)
    except StopIteration:
        pass

    return render_template("proj/projects.html", form=form, projects=results)    

@application.route("/projects/<int:site_id>")
@login_required
def view_project(site_id=None):
    
    query = Project.query.filter(Project.id == site_id)
    data = query_to_list(query)
    return render_template("proj/project.html", visits=data)

_LINK = Markup('<a href="{url}">{name}</a>')

def _make_link(site_id):
    url = url_for(".view_project", site_id=site_id)
    return _LINK.format(url=url, name=site_id)
