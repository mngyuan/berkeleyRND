# help from
# Flask mega tutorial
# http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates

# init setup

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app import views