import unittest
from DatabaseFunctions import *
from bjObjects import *
import json
import copy
import mongomock

tPath = '/Users/kjones/PycharmProjects/Blackjack4/Test/TestData/TestStateObjects.json'
testDict = {}
with open(tPath) as file:
	testDict =json.load(file)
gameInfo = testDict["gameInfo"]
newGameInfo = testDict["newGameInfo"]
playerDoc = testDict["playerDoc"]

class TestDBFunctions(unittest.TestCase):
	#expects mock collection to have appended 1 player object
	def test_initializePlayer(self):
		tName, tCookie = "Floppy", "123123123"
		collection = mongomock.MongoClient().testDB.Players
		initializePlayer(collection, tName, tCookie)
		results = collection.count_documents({"name": tName, "cookie": tCookie})
		self.assertEqual(results,1,"one result should exist in temp collection")

	#expects mock collection to have new Game info with unique ID
	def test_initializeGameInfo(self):
		cookie = "123123123"
		collection = mongomock.MongoClient().testDB.GameInfo
		id = initializeGameInfo(collection,cookie)
		results = collection.find()
		logic = results[0]["ID"] == id and len(results[0]["playerCookies"]) != 0
		self.assertTrue(logic,"failed to create a doc with unique ID and appended player cookie")

	#confirms update gameinfo works by changing the state field
	def test_updateGameInfo(self):
		#builds mock coll with 1 document
		collection = mongomock.MongoClient().testDB.GameInfo
		original = gameInfo
		collection.insert_one(original)

		id = original["ID"]
		update = {"state": "changed"}
		updateGameInfo(collection,id,update)

		newDoc = collection.find()[0]
		self.assertNotEqual(newDoc, original, "Update failed to happen if docs equal")

	#confirms update of the player currentHand
	def test_updatePlayer(self):
		#builds mock coll with 1 document
		collection = mongomock.MongoClient().testDB.Players
		original = playerDoc
		collection.insert_one(original)

		cookie = original["cookie"]
		diff = copy.copy(original)
		diff["name"] = "madame Dame Judy Dench"
		updatePlayer(collection,cookie,diff)

		newDoc = collection.find()[0]
		logic = (newDoc != original) and (newDoc["cookie"]==original["cookie"])
		self.assertTrue(logic, "Update failed to happen if docs equal or cookie has changed")

	def test_mongoCardDecoder(self):
		card = mongoCardDecoder({'suit': 'H', 'value': 5})
		outcome = Card("H",5)
		self.assertIsNotNone(card, "Fails if new player not generated")
		self.assertEqual(card,outcome,"expected cards aren't correct, failed to import")

	#note: uses copy.copy to avoid dictionary mutable issues
	def test_mongoHandDecoder(self):
		hand = mongoHandDecoder(copy.deepcopy(playerDoc["hands"][0]))
		self.assertEqual(hand.hand[0],Card("C",7),"expected cards aren't correct, failed to import")
		self.assertTrue(hand.hitState==0,"should pass if hand hit 0 times")
		self.assertTrue(hand.double==1, "should pass if hand did double")

	#note: uses copy.copy to avoid dictionary mutable issuess
	def test_mongoPlayerDecoder(self):
		player = mongoPlayerDecoder(copy.deepcopy(playerDoc))
		self.assertIsNotNone(player, "Fails if new player not generated")
		self.assertTrue(player.hands[0].hand[0].value==7,"fails if array of Hands not generated or first card != 7")
		self.assertTrue(player.currentHand.hand[0].value==12,"fails if array of Hands not generated or first card != 7")


