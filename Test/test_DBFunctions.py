import unittest
from DatabaseFunctions import *
from bjObjects import *
import json

tPath = '/Users/kjones/PycharmProjects/Blackjack4/Test/TestData/TestStateObjects.json'
testDict = {}
with open(tPath) as file:
	testDict =json.load(file)
gameInfo = testDict["gameInfo"]
playerDoc = testDict["playerDoc"]

testColl = LaunchCollConnection("UnitTest", "Players")

class TestDBFunctions(unittest.TestCase):
	#expects dictionary to have appended 1 player object
	def test_initializePlayer(self):
		tName, tCookie = "Floppy", "123123123"
		initializePlayer(testColl, tName, tCookie)

	def test_mongoCardDecoder(self):
		card = mongoCardDecoder({'suit': 'H', 'value': 5})
		outcome = Card("H",5)
		self.assertIsNotNone(card, "Fails if new player not generated")
		self.assertEqual(card,outcome,"expected cards aren't correct, failed to import")

	def test_mongoHandDecoder(self):
		hand = mongoHandDecoder(playerDoc["hands"][0])
		print(hand.hand[0])
		self.assertEqual(hand.hand[0],Card("C",7),"expected cards aren't correct, failed to import")
		self.assertTrue(hand.hitState==0,"should pass if hand hit 0 times")
		self.assertTrue(hand.double==1, "should pass if hand did double")

	#todo: mutable issue again
	def test_mongoPlayerDecoder(self):
		player = mongoPlayerDecoder(playerDoc)
		self.assertIsNotNone(player, "Fails if new player not generated")
		self.assertTrue(player.hands[0].hand[0].value==7,"fails if array of Hands not generated or first card != 7")
		self.assertTrue(player.currentHand.hand[0].value==12,"fails if array of Hands not generated or first card != 7")


