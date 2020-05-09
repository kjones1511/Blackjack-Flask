from ServerGameFunctions import *
from DatabaseFunctions import *
import json
# Dictionary Player asks to start hand, builds new hand that includes new dealer hand
# receives API request with player & session info
# returns
# todo: move this function to a new gameStates file
# todo: remember that currently function handles 1 player (in JSON), needs to handle array of players

#todo: append UUID to playerDoc
def startHand(players, deckCount):
	#todo: figure out how to handle Dealer in dealFirstHand()
	dealerHand = Hand()
	#todo: add JS message welcoming start of game
	###INITIALIZE phase
	#creates a deck, with deckCount decided by casino
	deck = initializeDeck(deckCount)
	dealHand(players, dealerHand, deck)

	#TODO add code to record decks

	#TODO: 1 second of initially showing cards

def pushHit(self):
	self.fail()


def pushDouble(self):
	self.fail()


def pushStand(self):
	self.fail()


def pushSplit(self):
	self.fail()