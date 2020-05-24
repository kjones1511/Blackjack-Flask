from ServerGameFunctions import *
from DatabaseFunctions import *
import json
# Dictionary Player asks to start hand, builds new hand that includes new dealer hand
# receives API request with player & session info
# returns
# todo: move this function to a new gameStates file
# todo: remember that currently function handles 1 player (in JSON), needs to handle array of players

#todo: currently points at Test DB
DB = "TestObjects"
collGameInfo = LaunchCollConnection(DB,"gameInfo")
collPlayers = LaunchCollConnection(DB,"Players")
ID = "edbd9d8a-9244-11ea-bb37-0242ac130002"


#doesn't request player data if state is wait
	#uses cookie to refer to 1 player, need to modify for multiple players
	#runs each state, resets game state to wait afterwords
def gameloop():
	count = 0
	notGameOver = True
	while notGameOver:
		stateHandler(ID)
		time.sleep(.1)
		count += 1
		print(count)


def stateHandler(ID):
	gameInfoJSON = requestGameStateMongo(collGameInfo, ID)
	state = gameInfoJSON["state"]
	if  state == "wait":
		return state

	cookie = gameInfoJSON["playerCookies"][0]
	playerJSON = requestPlayerMongo(collPlayers,cookie)
	print(state)
	if state == "startHand":
		print("startHand state")
		newplayerJSON = startHand(playerJSON, gameInfoJSON)
	if state == "hit":
		print("hit state")

	gameInfoJSON["state"] = "wait"
	updateGameInfo(collGameInfo, ID, gameInfoJSON)
	updatePlayer(collPlayers,cookie, newplayerJSON)
	return "changed"

#todo: append UUID to playerDoc
#todo: playerJSON is destroyed when decoding, find a more elegant solution
#todo: record deck as game Info item, fix deck to populate from JSON
def startHand(playerJSON, gameInfoJSON):
	deckCount = gameInfoJSON["deckCount"]
	#build player from JSON, make a deck, run function
	player = mongoPlayerDecoder(playerJSON)
	deck = initializeDeck(deckCount)
	dealHand(player, deck)
	#update JSON (gameInfo updated in top layer)
	newPlayerJSON = objToDict(player)
	gameInfoJSON["deck"] = objToDict(deck)
	return newPlayerJSON


	#TODO add code to record decks


def pushHit(playerJSON, gameInfoJSON):
	playerCookies = gameInfo["playerCookies"]
	players = []

	return


def pushDouble():
	return

def pushStand():
	return

def pushSplit():
	return

if __name__ == '__main__':
	gameloop()
