import json
from pymongo import *
from bjObjects import *
import dns
#import pprints

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
    result = coll.find({"name": player, "cookie": cookie})
    #if result.retrieved != 0:
    for item in result:
        print(item)

def MongoDecoder(studentDict):
    return namedtuple('X', studentDict.keys())(*studentDict.values())


if __name__ == '__main__':
    test = {"test":1}

    coll = LaunchCollConnection("Results","Players")
    result = requestPlayerMongo(coll, "Floppy","123123123")
    
    #clears collection
    #coll.delete_many({})


