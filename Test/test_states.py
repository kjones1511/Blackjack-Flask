import unittest
import mongomock
from States import *
import json

tPath = '/Users/kjones/PycharmProjects/Blackjack4/Test/TestData/TestStateObjects.json'
testDict = {}
with open(tPath) as file:
	testDict =json.load(file)
gameInfo = testDict["gameInfo"]
gameInfo2 = testDict["gameInfo2"]
playerDoc = testDict["playerDoc"]
newGameInfo = testDict["newGameInfo"]
newPlayerDoc = testDict["newPlayerDoc"]

class TestStates(unittest.TestCase):

	#for later
	def signIn(self):
		return

	#Won't do anything initially, but need to plan for making tables for multiple games happening concurrently
	def launchTable(self):
		return


	#todo, too hard to test main game loop without real collections at this point
	def test_stateHandler(self):
		self.assertTrue(True, "shouldn't throw an error ever")


	#returned JSON should have new player & dealer cards
	def test_startHand(self):
		#initial expected JSON should be a playerDoc with empty hand
		logic1 = len( newPlayerDoc["currentHand"][0]["hand"] ) == 0
		print( newPlayerDoc["currentHand"][0] )

		self.assertTrue(logic1, "fails if test JSON has no hand field or hand is populated")
		#returns with JSON to update
		newPlayerJSON = startHand(newPlayerDoc, gameInfo)
		print( newPlayerJSON)

		logic2a = len( newPlayerJSON["currentHand"][0]["hand"] ) == 2
		logic2b = len( newPlayerJSON["currentHand"][0]["dealerHand"][0]["hand"] ) == 2
		logic2 = logic2a and logic2b
		self.assertTrue(logic2, "fails if test JSON has not been updated with 2 cards for player & dealer")


	def test_pushHit(self):
		deckSize = len( gameInfo["deck"]["cards"])
		oldScore = playerDoc["currentHand"][0]["score"]

		newPlayerDoc = pushHit(playerDoc, gameInfo)
		deckSizeChange  = len( gameInfo["deck"]["cards"]) - deckSize
		scoreChange = newPlayerDoc["currentHand"][0]["score"] - oldScore

		logic1 = len (newPlayerDoc["currentHand"][0]["hand"]) == 3
		logic2 = deckSizeChange == -1
		logic3 = scoreChange !=0
		self.assertTrue(logic1 and logic2 and logic3, "fails if player has less than 3 cards, or if deck size isn't reduced by 1")


	def test_pushDouble(self):
		self.fail()


	def test_pushStand(self):
		self.fail()


	def test_pushSplit(self):
		self.fail()

# TODO add code to record decks

# TODO: 1 second of initially showing cards



if __name__ == '__main__':
	unittest.main()
