from rndapp import app, db

app.debug = True
db.create_all(app=app)
app.run()
