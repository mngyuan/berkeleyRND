import config

# startup
# this will also load config.py
from rndapp import app

app.run(debug = config.DEBUG)