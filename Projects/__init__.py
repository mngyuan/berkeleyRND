from flask import Flask

from .auth import login_manager
from .data import db
from .proj.views import application
from .users.views import users

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)

login_manager.init_app(app)

app.register_blueprint(application)
app.register_blueprint(users)
