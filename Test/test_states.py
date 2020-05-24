import unittest
from States import *
import json

tPath = '/Users/kjones/PycharmProjects/Blackjack4/Test/TestData/TestStateObjects.json'
testDict = {}
with open(tPath) as file:
	testDict =json.load(file)
gameInfo = testDict["gameInfo"]
newGameInfo = testDict["newGameInfo"]
newPlayerDoc = testDict["newPlayerDoc"]

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

	def test_stateHandler(self):
		#stateHandler("edbd9d8a-9244-11ea-bb37-0242ac130002")
		self.fail()


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
		self.fail()


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
