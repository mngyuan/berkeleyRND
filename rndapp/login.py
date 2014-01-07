from wtforms import Form, TextField, PasswordField, validators

# class LoginForm(Form):
#     openid = TextField('openid', validators = [Required()])
#     remember_me = BooleanField('remember_me', default=False)

class LoginForm(Form):
	login = TextField([validators.Required()])
	password = PasswordField([validators.Required()])

	def get_user(self):
		return db.session.query(User).filter_by(login=self.login.data).first()

	def validate_login(self, field):
		# called upon a login attempt
		user = self.get_user()

		if user is None:
			raise validators.ValidationError('Invalid user!')
		if user.password != self.password.data:
			raise validators.ValidationError('Invalid password!')

class RegistrationForm(Form):
	loginuname = TextField('Username', [validators.Required()])
	password = PasswordField('Password', [
		validators.Required(),
		validators.EqualTo('confirm', message='Passwords must match')
	])
	confirmpw = PasswordField('Repeat password')
	firstname = TextField()
	lastname = TextField()

	email = TextField([validators.Required(), validators.Email()])

	def validate_login(self, field):
		if db.session.query(User).filter_by(login=self.login.data).count() > 0:
			raise validators.ValidationError('Username in use!')

		# TODO: also need to validate berkeley.edu


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