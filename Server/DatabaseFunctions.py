import json
from pymongo import *
from bjObjects import *
import dns
#import pprints


tempDict = {'name': 'Floppy',
            'cookie': '123123123',
            'money': 1000,
            'hands': [],
            'currentHand': [
                {'hand': [], 'blackjack': 0, 'win': 0, 'split': 0, 'double': 0, 'hitState': 0, 'dealerHand': [], 'dealerScore': 0, 'score': 0, 'originalScore': 0}
            ]}

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

    #should initialize to Players collection
def initializePlayer(coll, player,cookie):
    #todo: delete after added collection coll = LaunchCollConnection( "Players")
    result = coll.count_documents({"name": player, "cookie": cookie})
    if result == 0:
        tempPlayer = Player(player,cookie)
        playerJSON = objToDict(tempPlayer)
        coll.insert_one(playerJSON)

    #todo: returns JSON currently, needs to return object
def requestPlayerMongo(coll, player,cookie):
    result = coll.find({"name": player, "cookie": cookie},{"_id":0})
    #if result.retrieved != 0:
    for item in result:
        print(item)

#        print(item["currentHand"])

    #will convert a dict Hand to Hand object, requires iterating over hand array
def mongoCardDecoder(mongoDict):
    print(mongoDict)
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

#    return namedtuple('X', studentDict.keys())(*studentDict.values())


if __name__ == '__main__':
    # test = {"test":1}
    #
    # coll = LaunchCollConnection("Results","Players")
    # result = requestPlayerMongo(coll, "Floppy","123123123")
    mongoDecoder(tempDict)
    #clears collection
    #coll.delete_many({})


