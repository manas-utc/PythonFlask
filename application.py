from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def index():
    return "Hello World from Flask !! Hurray"
 
@app.route("/hello")
def hello():
    return "Hello World!"
 
@app.route("/members")
def members():
    return "Members"
 
@app.route("/members/<string:name>/")
def getMember(name):
    return "Hello " + name