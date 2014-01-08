from werkzeug.security import generate_password_hash, check_password_hash
from rndapp import db

# User model in db
class User(db.Model):
	# defining rows in the user table
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(100))
	last_name = db.Column(db.String(100))
	loginuname = db.Column(db.String(80), unique=True)
	email = db.Column(db.String(120))
	# TODO: password salts, password hashing.
	password = db.Column(db.String(64))

	def __init__(self):
		# registering makes new user objects
		# TODO: this should do seomthing.
		pass

	# Flask-Login
	def is_authenticated(self):
		return True

	def is_active(self):\
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

	# TODO integrate this
	def set_password(self, pw):
		self.pw_hash = generate_password_hash(pw)

	def check_password(self, pw):
		return check_password_hash(self.pw_hash, pw)