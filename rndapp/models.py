from werkzeug.security import generate_password_hash, check_password_hash
from rndapp import db

# User model in db
class User(db.Model):
	# defining rows in the user table
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(100))
	last_name = db.Column(db.String(100))
	loginuname = db.Column(db.String(80), unique=True)
	email = db.Column(db.String(120), unique=True)
	pw_hash = db.Column(db.String(64))

	projs = db.relationship('Project', backref='poster', lazy='dynamic')

	def __init__(self, login, password, first_name, last_name, email):
		# is that all this has to do?
		# why are some files tabs and some 4 spaces?
		# is there a greater purpose to life?
		# will anyone really ever read this?
		# is hilfinger a god or a demon?
		self.loginuname = login
		self.pw_hash = self.set_password(password)
		self.first_name = first_name
		self.last_name = last_name
		self.email = email

	# Flask-Login
	def is_authenticated(self):
		return True

	def is_active(self):
		# disables login if False
		# doubt we'll implement inactive user functionality?
		# maybe email verification?
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return unicode(self.id)

	def __repr__(self):
		return "<USER %r>"%(self.loginuname)

	# Salted and hashed pw from werkzeug
	def set_password(self, pw):
		self.pw_hash = generate_password_hash(pw)

	def check_password(self, pw):
		return check_password_hash(self.pw_hash, pw)


# declaring, not implementing yet.
class Project(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(64))
	desc = db.Column(db.String(256))
	timestamp = db.Column(db.DateTime)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return '<Project %r>'%(self.title)
