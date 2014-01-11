from wtforms import Form, TextField, PasswordField, validators
from rndapp import db
from models import User

# class LoginForm(Form):
#     openid = TextField('openid', validators = [Required()])
#     remember_me = BooleanField('remember_me', default=False)

class LoginForm(Form):
	login = TextField('Username')
	password = PasswordField('Password')

	def get_user(self, form):
		return User.query.filter_by(loginuname=form.login.data).first()
		# return db.session.query(User).filter_by(loginuname=form.login.data).first()

	def validate_login(form, field):
		# this gets run by the validate() chain
		# HOW? WHY IS THIS FUNCTIONALITY NOT DOCUMENTED? WHELL HERE GOES
		# VALIDATE() FROM FORM:
		# RUNS INLINE VALIDATORS BASED ON CLASS ATTR NAMES:
		#   inline = getattr(self.__class__, 'validate_%s' % name, None)
		# UGH
		user = form.get_user(form)

		if user is None: # consider consolidating w/ pw check for security
			raise validators.ValidationError('Invalid user!')
			# self.errors[self.login] = 'Invalid user!'

	def validate_password(form, field):
		user = self.get_user(self)
		if user and not user.check_password(field.data):
			raise validators.ValidationError('Invalid password!')
			# self.errors[self.password] = 'Invalid password!'


class RegistrationForm(Form):
	loginuname = TextField('Username', [validators.Required()])
	password = PasswordField('Password', [
		validators.Required(),
		validators.EqualTo('confirmpw', message='Passwords must match')
	])
	confirmpw = PasswordField('Repeat password')
	firstname = TextField()
	lastname = TextField()
	email = TextField('berkeley.edu email', [validators.Required(), validators.Email()])

	def validate_loginuname(self, field):
		if db.session.query(User).filter_by(loginuname=self.loginuname.data).count() > 0:
			raise validators.ValidationError('Username in use!')
		# TODO: also need to validate berkeley.edu

