from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return  "please god work" #render_template("about.html")

import Flask.Routes.routes

