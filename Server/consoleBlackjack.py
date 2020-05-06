from GameFunctions import *
from DatabaseFunctions import *

# initialize
choice = ""
clear()
players = []
data = {
	"player": "",
	"casino": "",
	"hands": []  #format of each hand. timestamp, playerHand Arr, dealerHand Arr, win (1/0), #hits, #doubles
}

#temp
casino = "La Casa De Mi Padre"
deckCount = 2
dealerStandBoundary = 17

def game():
	#get mongoDB collection pointer
	coll = LaunchCollConnection()

	#todo: figure out how to handle Dealer in dealFirstHand()
	dealerHand = Hand()

	print ("WELCOME TO BLACKJACK!\n")

	###INITIALIZE phase
	#creates a deck, with deckCount decided by casino
	initializeOnePlayer(players, data, casino)
	deck = initializeDeck(deckCount)

	dealHand(players, dealerHand, deck)

	#TODO add code to record decks

	#TODO: 1 second of initially showing cards

	#main game loop - runs until request to quit or no players
	while len(players) != 0 or choice != "q":

		#shuffles deck if running low
		if len(deck.cards) < 30:
			deck = Deck(deckCount)

		#check for dealer blackjack. Called this before showing the dealer hand because it's weird to announce their top card then BJ
		#TODO: eventually, end the round at this point if dealer blackjack. Blackjack logic currently busted ,only checks player 0
		blackjack(dealerHand, players[0])
		print("The dealer is showing a " + str(dealerHand.hand[0]))

		#handle splits
		#option to hit per hand
		for player in players:
			player.splitLogic(deck)

			#decision-making logic for each player hand
			for thisHand in player.currentHand:
				clear()
				playerDecisionHandling (thisHand, dealerHand, player, deck)

		#resolve dealer hand
		dealerHitlogic(dealerHand, dealerStandBoundary, deck)

		#Score, Record & give a chance to leave the game at any time, or after rounds
		#NOTE: Scoring shouldn't occur if there are 0 players in game
		for player in players:
			for thisHand in player.currentHand:
				clear()
				#check for winner
				score(dealerHand, thisHand)

				#compress hand to JSON, append to dictionary
				x = json.dumps(thisHand.__dict__, default=lambda o: o.__dict__)
				data["hands"].append(  json.loads(x)  )

				#TODO: unless i decide to compress the whole player, this line is unecessary
				player.hands.append(thisHand)

				time.sleep(2.5)

			choice = input("Do you want to [C]ontinue or [Q]uit: ").lower()
			if choice == "q":
				#pushes data JSON to collection, todo make this work for mult players by requesting data per player
				coll.insert_one( data )
				players.remove( player )
				print("Goodbye" + player.name + "!")
				#print(data)

		#deal new hands
		dealHand(players, dealerHand, deck)
		# for player in players:
		# 	player.currentHand = [Hand()]
		# 	player.currentHand[0].newHand(deck)
		# dealerHand.newHand(deck)
		clear()
	exit()

def test():
	client = MongoClient(
		"mongodb+srv://root:chicago1%21@blackjackanalytics-idjco.mongodb.net/Results?retryWrites=true&w=majority&authSource=admin")
	db = client.Results
	coll = db.TestColResults

	player = Player("kile", 100)
	card1 = Card("S", 7)
	card2 = Card("D", 7)
	card3 = Card("D", 7)
	deck = Deck(2)
	deck.shuffle()
	hand = Hand()
	player.currentHand.append(hand)
	player.currentHand[0].hand = [card1, card2, card3]

	data = {
		"player": "take2",
		"casino": "",
		"hands": []  # format of each hand. timestamp, playerHand Arr, dealerHand Arr, win (1/0), #hits, #doubles
	}

	for hand in player.currentHand:
		data = json.dumps(player.__dict__, default=lambda o: o.__dict__)
		coll.insert_one(data)


# print( vars(card1) )
# print(vars(player.currentHand[0]))


if __name__ == "__main__":
	game()
	#test()