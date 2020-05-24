from flask import Flask, render_template, request, jsonify
from bjObjects import *
# Create some test data for our catalog in the form of a list of dictionaries.

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return  "please god work" #render_template("about.html")

import Flask.Routes.routes

