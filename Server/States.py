# Dictionary Player asks to start hand, builds new hand that includes new dealer hand
# receives API request with player & session info
# returns
# todo: move this function to a new gameStates file
# todo: remember that currently functino handles 1 player (in JSON), needs to handle array of players
def StartHand():
	# todo: check if player exists in DB before building new document
	##This may be a separate, post delivery job

	dealerHand = Hand()

	print("WELCOME TO BLACKJACK!\n")

	###INITIALIZE phase
	# creates a deck, with deckCount decided by casino
	initializeOnePlayer(players, data, casino)
	deck = initializeDeck(deckCount)

	dealHand(players, dealerHand, deck)


def pushHit(self):
	self.fail()


def pushDouble(self):
	self.fail()


def pushStand(self):
	self.fail()


def pushSplit(self):
	self.fail()