from rndapp import app, db
import config

app.debug = config.DEBUG
db.create_all(app=app)
app.run()
