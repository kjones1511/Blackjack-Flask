from Flask.main import app
from flask import render_template, request, jsonify
from API import *
from DatabaseFunctions import *

DB = "TestObjects"


@app.route("/test")
def test():
	return {"body": "FUUUUUCCKKKKK"}


@app.route("/tableUpdate/<string:cookie>")
def tableUpdate(cookie):
	coll = LaunchCollConnection(DB, "Players")
	result = requestPlayerMongo(coll, cookie)
	response = jsonify(result)
	response.headers.add('Access-Control-Allow-Origin', '*')
	return (response)

@app.route("/gameInfoUpdate/<string:ID>")
def gameInfoUpdate(ID):
	coll = LaunchCollConnection(DB, "gameInfo")
	result = requestGameStateMongo(coll, ID)
	response = jsonify(result)
	response.headers.add('Access-Control-Allow-Origin', '*')
	return (response)


# return result

@app.route("/json", methods=["POST"])
def json():
	return APIjson(request)


@app.route('/hit', methods=["POST"])
def hit():
	return APIGameStateChange(request, "hit")


@app.route('/double', methods=["POST"])
def double():
	return APIGameStateChange(request, "double")


@app.route('/split', methods=["POST"])
def split():
	return APIGameStateChange(request, "split")


@app.route('/stand', methods=["POST"])
def stand():
	return APIGameStateChange(request, "stand")


@app.route('/addPlayer/<string:name>')
def addPlayer(name):
	# todo: make a function, logical to avoid duplicating results
	coll = LaunchCollConnection(DB, "Players")
	initializePlayer(coll, name, "56565656565656")
	return ("succeeded")


@app.route('/testPlayer')
def testPlayer():
	tJson = {
		"playerDoc": {
			"name": "Kody",
			"cookie": "ASDKASDSDKSADADKAKDS",
			"money": 5555,
			"hands": [
				{"hand":
					 [{"suit": "C", "value": 7}, {"suit": "C", "value": 4}, {"suit": "C", "value": 12}],
				 "blackjack": 0,
				 "win": 1,
				 "split": 0,
				 "double": 1,
				 "hitState": 0,
				 "dealerHand": [{"suit": "H", "value": 8}, {"suit": "C", "value": 9}],
				 "dealerScore": 17,
				 "score": 21,
				 "originalScore": 11,
				 "timestamp": "8/20/2020 2:40 PM"}
			],
			"currentHand": [
				{"hand": [{"suit": "C", "value": 12}, {"suit": "H", "value": 5}],
				 "blackjack": 0,
				 "win": 0,
				 "split": 0,
				 "double": 0,
				 "hitState": 1,
				 "dealerHand": [
					 {"suit": "H", "value": 12},
					 {"suit": "D", "value": 6},
					 {"suit": "C", "value": 8}
				 ],
				 "dealerScore": 24,
				 "score": 23,
				 "originalScore": 7,
				 "timestamp": "8/20/2020 2:40 PM"
				 }]}}
	response = jsonify(tJson)
	response.headers.add('Access-Control-Allow-Origin', '*')
	return (response)


@app.route('/testGameState')
def testGameState():
	tJson = {
		"gameInfo": {
			"ID": "edbd9d8a-9244-11ea-bb37-0242ac130002",
			"state": "gameOver",
			"choice": "",
			"casino": "La Casa De Mi Padre",
			"deckCount": 2,
			"dealerStandBoundary": 17,
			"playerCookies": ["123123123"],
			"deck": ""
		}}
	response = jsonify(tJson)
	response.headers.add('Access-Control-Allow-Origin', '*')
	return (response)
