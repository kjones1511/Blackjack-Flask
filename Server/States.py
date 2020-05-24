from ServerGameFunctions import *
from DatabaseFunctions import *
import json
# Dictionary Player asks to start hand, builds new hand that includes new dealer hand
# receives API request with player & session info
# returns
# todo: move this function to a new gameStates file
# todo: remember that currently function handles 1 player (in JSON), needs to handle array of players

#todo: currently points at Test DB
collGameInfo = LaunchCollConnection("TestObjects","gameInfo")
collPlayers = LaunchCollConnection("TestObjects","Players")

	#doesn't request player data if state is wait
	#uses cookie to refer to 1 player, need to modify for multiple players
def stateHandler(ID):
	gameInfo = requestGameStateMongo(collGameInfo, ID)
	state = gameInfo["state"]
	if  state == "wait":
		return state
	print("cookie")
	if state == "hit":
		print("hit state")
		pushHit(gameInfo)
	return state

#todo: append UUID to playerDoc
def startHand(gameInfo):
	deckCount = gameInfo["deckCount"]
	cookie = gameInfo["playerCookies"][0]

	#todo: figure out how to handle Dealer in dealFirstHand()
	dealerHand = Hand()
	mongoDict = requestPlayerMongo(collGameInfo, cookie)
	player = mongoPlayerDecoder(mongoDict)

	###INITIALIZE phase
	#creates a deck, with deckCount decided by casino
	deck = initializeDeck(deckCount)
	dealHand(player, deck)

	#TODO add code to record decks


def pushHit(gameInfo):
	playerCookies = gameInfo["playerCookies"]
	players = []
	for cookie in playerCookies:
		players.append( )
	return


def pushDouble():
	return

def pushStand():
	return

def pushSplit():
	return