from DatabaseFunctions import *
import unittest
from ServerGameFunctions import *
import json

tPath = '/Users/kjones/PycharmProjects/Blackjack4/Test/TestData/TestStateObjects.json'
testDict = {}
with open(tPath) as file:
	testDict = json.load(file)

gameInfo = testDict["gameInfo"]
newPlayer = testDict["newPlayerDoc"]


# test array
# for test_str, checks that the card object prints the string in 2nd element of array pairs
# for test_equal, compares pairs of initial array elements for equality


# todo: test for initializeOnePlayer(gameInfo,players)

class TestGame(unittest.TestCase):
	#expects dictionary to have appended 1 player object
	def test_dealHand(self):
		deck = Deck(2)
		player = mongoPlayerDecoder(newPlayer)

		logic1 = len(player.currentHand[0].hand) == 0 and len(player.currentHand[0].dealerHand) == 0
		self.assertTrue(logic1, "fails if new player has cards or dealerHand is populated")

		dealHand(player, deck)
		logic2 = len( player.currentHand[0].hand ) == 2  and len( player.currentHand[0].dealerHand[0].hand ) == 2
		self.assertTrue(logic2,"fails if new player/deal hand don't have 2 cards")


if __name__ == '__main__':
	unittest.main()
