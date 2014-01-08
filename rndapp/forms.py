from wtforms import Form, TextField, PasswordField, validators
from rndapp import db

# class LoginForm(Form):
#     openid = TextField('openid', validators = [Required()])
#     remember_me = BooleanField('remember_me', default=False)

class LoginForm(Form):
	login = TextField('Username', [validators.Required()])
	password = PasswordField('Password', [validators.Required()])

	def get_user(self):
		return db.session.query(User).filter_by(loginuname=self.login.data).first()

	def validate_login(self, field):
		# i believe this is called when form.validate is called
		# but. need to verify these functions ever get called.
		user = self.get_user()

		if user is None:
			raise validators.ValidationError('Invalid user!')
		if user.password != self.password.data:
			raise validators.ValidationError('Invalid password!')

class RegistrationForm(Form):
	login = TextField('Username', [validators.Required()])
	password = PasswordField('Password', [
		validators.Required(),
		validators.EqualTo('confirm', message='Passwords must match')
	])
	confirmpw = PasswordField('Repeat password')
	firstname = TextField()
	lastname = TextField()
	email = TextField('berkeley.edu email', [validators.Required(), validators.Email()])

	def validate_login(self, field):
		if db.session.query(User).filter_by(loginuname=self.login.data).count() > 0:
			raise validators.ValidationError('Username in use!')

		# TODO: also need to validate berkeley.edu

