import os
import secret

DEBUG = True
ANALYTICS = False

CSRF_ENABLED = True
# the md5 of some text i randomly decided
SECRET_KEY = secret.key

# OPENID_PROVIDERS = [
#     { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
#     { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
#     { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
#     { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
#     { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]

# db config

# USERNAME = "admin"
# PASSWORD = "default"

SQLALCHEMY_ECHO = True # logs stderr
