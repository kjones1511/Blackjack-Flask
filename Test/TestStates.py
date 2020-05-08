import unittest
from States import *
import json

tPath = '/Users/kjones/PycharmProjects/Blackjack4/Test/TestData/TestStateObjects.json'
tJSON = {}
with open(tPath) as file:
	tJSON =json.load(file)

#todo: build fixture with player array

class TestStates(unittest.TestCase):

	#todo: make part of a fixture
	def test_JSONDataLoads(self):
		self.assertEqual(tJSON['test1'], {'name': 'Julian', 'message': 'Posting JSON data to Flask!'}, "test JSON didn't load")

	#for later
	def signIn(self):
		return

	#Won't do anything initially, but need to plan for making tables for multiple games happening concurrently
	def launchTable(self):
		return

	#ensures player ends up with new hand,
	def test_startHand(self):
		startHand()
		self.fail()

	def startHand(players, data, casino, deckCount):
		# todo: figure out how to handle Dealer in dealFirstHand()
		dealerHand = Hand()
		# todo: add JS message welcoming start of game
		###INITIALIZE phase
		# creates a deck, with deckCount decided by casino
		deck = initializeDeck(deckCount)
		dealHand(players, dealerHand, deck)

# TODO add code to record decks

# TODO: 1 second of initially showing cards



if __name__ == '__main__':
	unittest.main()
