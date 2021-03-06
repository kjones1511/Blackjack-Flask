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
		stateHandler(ID, collGameInfo, collPlayers)
		time.sleep(.1)
		count += 1
		print(count)

def gameONEloop():
	count = 0
	stateHandler(ID)
	time.sleep(.1)
	count += 1
	print(count)

#todo: quirk, playerJSON is mutated when decoding, need a new JSOON dictionary for recording
def stateHandler(ID, collGame, collPlayer):
	#check game state from GameInfo collection
	gameInfoJSON = requestGameStateMongo(collGame, ID)
	state = gameInfoJSON["state"]
	if  state == "wait":
		return state

	cookie = gameInfoJSON["playerCookies"][0]
	playerJSON = requestPlayerMongo(collPlayer,cookie)
	stateCalled = "changed"
	if state == "startHand":
		stateCalled = state
		print("startHand state")
		newplayerJSON = startHand(playerJSON, gameInfoJSON)
	elif state == "hit":
		stateCalled = state
		newplayerJSON = pushHit(playerJSON, gameInfoJSON)
	elif state == "gameOver":
		stateCalled = state
		resolveHand(playerJSON, gameInfoJSON)
	elif state == "split":
		stateCalled = state
		pass
	elif state == "double":
		stateCalled = state
		pass
	elif state == "stand":
		stateCalled = state
		pass
	if checkGameover(newplayerJSON, gameInfoJSON):
		gameInfoJSON["state"] = "gameOver"
	else:
		gameInfoJSON["state"] = "wait"

	#update related DB records
	updateGameInfo(collGame, ID, gameInfoJSON)
	updatePlayer(collPlayer,cookie, newplayerJSON)
	return stateCalled

#todo: append UUID to playerDoc
#todo: (repeat of todo in main loop) playerJSON is destroyed when decoding, find a more elegant solution
#todo: record deck as game Info item, fix deck to populate from JSON
#todo: doesn't address blackjack or splits
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

	#todo: assuming gameInfo will break on pushhit
	#will add card and calculate new score
def pushHit(playerJSON, gameInfoJSON):
	player = mongoPlayerDecoder(playerJSON)
	deck = mongoDeckDecoder(gameInfoJSON)
	player.currentHand[0].hit(deck)
	player.currentHand[0].newScore()
	player.currentHand[0].hitState = 1

	newPlayerJSON = objToDict(player)
	gameInfoJSON["deck"] = objToDict(deck)
	return newPlayerJSON


def pushDouble():
	return

def pushStand():
	return

def pushSplit():
	return

if __name__ == '__main__':
	gameloop()
