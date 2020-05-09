from API import *
from flask import Flask, render_template, request, jsonify
from bjObjects import *
from DatabaseFunctions import *
# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

# A route to return all of the available entries in our catalog.
def adder(a,b):
    return a + b

@app.route('/testPost')
def TestPost():
    if 'id' in request.args:
        id = int(request.args['id'])
        return jsonify( adder(2,id))
    else:
        return "Error: No id field provided. Please specify an id."

@app.route('/addPlayer/<string:name>')
def addPlayer(name):
    #todo: make a function, logical to avoid duplicating results
    coll = LaunchCollConnection("Results","Players")
    initializePlayer(coll,name,"234234234")
    return ("succeeded")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/serveCard")
def serveCard():
    tCard = Card("D",9)
    x = json.dumps(tCard.__dict__, default=lambda o: o.__dict__)
    return jsonify(x)

@app.route("/json", methods=["POST"])
def json():
    return APIjson(request)

if __name__ == "__main__":
    app.run('localhost',5000,debug=True)


