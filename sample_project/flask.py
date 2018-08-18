from flask import flask
app = flask(sample_app)

@app.route("/")
def hello():
    return "Hello World!"
