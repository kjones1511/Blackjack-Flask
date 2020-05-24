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
		coll = LaunchCollConnection("Results", "Players")
		player = requestPlayerMongo(coll, "56565656565656")
		print(player)
		player = mongoPlayerDecoder(player)
		print(player)
		self.fail()


if __name__ == '__main__':
	unittest.main()
