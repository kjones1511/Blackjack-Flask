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

	def test_stateHandler(self):
		stateHandler("edbd9d8a-9244-11ea-bb37-0242ac130002")
		self.fail()


	#ensures player ends up with new hand,
	def test_startHand(self):
		startHand()
		self.fail()


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
