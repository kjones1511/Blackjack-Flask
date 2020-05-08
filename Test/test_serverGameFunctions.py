#import TestData.GameFunctionsData as testData
import unittest
from ServerGameFunctions import *
import json

tPath = '/Users/kjones/PycharmProjects/Blackjack4/Test/TestData/TestStateObjects.json'
testDict = {}
with open(tPath) as file:
	testDict =json.load(file)

gameInfo = testDict["gameInfo"]

#test array
# for test_str, checks that the card object prints the string in 2nd element of array pairs
# for test_equal, compares pairs of initial array elements for equality


#todo: test for initializeOnePlayer(gameInfo,players)

class TestGame(unittest.TestCase):
    #expects dictionary to have appended 1 player object
    def test_initializeOnePlayer(self):
        initializePlayers(gameInfo, "TestBoy")
        logicTest = gameInfo["players"][-1].name == "TestBoy"
        self.assertTrue(logicTest, "Fails if no new player objects added")

if __name__ == '__main__':
    unittest.main()
