import json
from pymongo import *
from bjObjects import *
import uuid
import dns
#todo if States works without this delete, doesnt seem to need pprints
#import pprints

defaultGameInfo = {
	"ID": 0,
	"state": "new",
	"choice": "",
	"casino": "La Casa De Mi Padre",
	"deckCount": 2,
	"dealerStandBoundary": 17,
	"playerCookies": None,
	"deck": ""
	}

# begin mongoDB connection, returns collection pointer
def LaunchCollConnection(dbName, collName):
    client = MongoClient(
        "mongodb+srv://root:chicago1%21@blackjackanalytics-idjco.mongodb.net/Results?retryWrites=true&w=majority&authSource=admin")
    #db = client.Results
    db = client[dbName]
    coll = db[collName]
    return coll

#recurisively converts all objects & their values to dictionary
def objToDict(obj):
    if not  hasattr(obj,"__dict__"):
        return obj
    result = {}
    for key, val in obj.__dict__.items():
        if key.startswith("_"):
            continue
        element = []
        if isinstance(val, list):
            for item in val:
                element.append(objToDict(item))
        else:
            element = objToDict(val)
        result[key] = element
    return result

    #if player doesn't exist, should initialize new player ID to the Players collection
    #returns True if successful
def initializePlayer(coll, player,cookie):
    #todo: delete after added collection coll = LaunchCollConnection( "Players")
    result = coll.count_documents({"name": player, "cookie": cookie})
    if result == 0:
        tempPlayer = Player(player,cookie)
        playerJSON = objToDict(tempPlayer)
        coll.insert_one(playerJSON)
        return True
    return False

def initializeGameInfo(coll,cookie):
    id = uuid.uuid1()
    defaultGameInfo["ID"] = id
    defaultGameInfo["playerCookies"] = [cookie]
    coll.insert_one(defaultGameInfo)
    return id

def updateGameInfo(coll, id, update):
    coll.update_one({"ID": id}, {"$set": update})

def updatePlayer(coll, cookie, update):
    return
    #filter = {"name:" name, "cookie": cookie}
    #coll.update_one(filter,update)


    #todo: returns JSON currently, needs to return object
def requestPlayerMongo(coll, player,cookie):
    result = coll.find({"name": player, "cookie": cookie},{"_id":0})
    #if result.retrieved != 0:
    for item in result:
        print(item)

#        print(item["currentHand"])

    #will convert a dict Hand to Hand object, requires iterating over hand array
def mongoCardDecoder(mongoDict):
    card = Card(**mongoDict)
    return card

def mongoHandDecoder(mongoDict):
    fixCards = []
    for card in mongoDict["hand"]:
        fixCards.append(mongoCardDecoder(card))
    mongoDict["hand"] = fixCards
    hand = Hand(**mongoDict)
    return hand

def mongoPlayerDecoder(mongoDict):
    #todo: in place repair hands array
    fixHands = []
    for hand in mongoDict["hands"]:
        fixHands.append( mongoHandDecoder(hand))
    mongoDict["hands"] = fixHands

    mongoDict["currentHand"] =  mongoHandDecoder(mongoDict["currentHand"])
    player = Player(**mongoDict)
    return player


if __name__ == '__main__':
    print("running main")

