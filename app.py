from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello Flask! Heroku.</p>"

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")




