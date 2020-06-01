from ConsoleGameFunctions import *

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

				#compress hand to JSON, append to dictionary. For saving to file eventually
				x = json.dumps(thisHand.__dict__, default=lambda o: o.__dict__)
				data["hands"].append(  json.loads(x)  )

				time.sleep(2)

			choice = input("Do you want to [C]ontinue or [Q]uit: ").lower()
			if choice == "q":
				players.remove( player )
				print("Goodbye " + player.name + " !")
				print(data)
				time.sleep(2)

		#deal new hands
		dealHand(players, dealerHand, deck)
		clear()
	exit()

if __name__ == "__main__":
	game()
	#test()