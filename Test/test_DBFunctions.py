import unittest
from DatabaseFunctions import *
from bjObjects import *
import json

tPath = '/Users/kjones/PycharmProjects/Blackjack4/Test/TestData/TestStateObjects.json'
testDict = {}
with open(tPath) as file:
	testDict =json.load(file)
gameInfo = testDict["gameInfo"]

testColl = LaunchCollConnection("UnitTest", "Players")

class TestDBFunctions(unittest.TestCase):
	#expects dictionary to have appended 1 player object
	def test_initializePlayer(self):
		tName, tCookie = "Floppy", "123123123"
		initializePlayer(testColl, tName, tCookie)

