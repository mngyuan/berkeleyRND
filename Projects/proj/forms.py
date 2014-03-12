from datetime import datetime as dt

from flask.ext.wtf import Form
from wtforms import fields
from wtforms.validators import Required
from wtforms.ext.sqlalchemy.fields import QuerySelectField

class ProjectForm(Form):
	title = fields.StringField(validators=[Required()])
	description = fields.StringField(validators=[Required()])