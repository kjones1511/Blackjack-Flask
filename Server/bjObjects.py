import random
import os
import time
from datetime import datetime
import json
#todo: destructors?

#clears terminal, for debugging only (TODO: remove functions like this in prod?)
def clear():
	if os.name == 'nt':
		os.system('CLS')
	if os.name == 'posix':
		os.system('clear')

class Card:
	#suit is string, value should be integer
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	def __str__(self):
		pVal = self.value
		if self.value == 11: pVal = "J"
		elif self.value == 12: pVal = "Q"
		elif self.value == 13: pVal = "K"
		elif self.value == 14: pVal = "A"
		return "[" + self.suit + ", " + str(pVal) + "]"

	#note: equality is checking suit and value (for ensuring a deck is shuffled). No current method for checking just value equality
	def __eq__(self, other):
		"""Overrides the default implementation"""
		if isinstance(other, self.__class__):
			return (self.suit == other.suit and self.value == other.value)
		return NotImplemented

class Hand:
	# def __init__(self, *initial_data, **kwargs):
	# 	for dictionary in initial_data:
	# 		for key in dictionary:
	# 			setattr(self, key, dictionary[key])
	# 	for key in kwargs:
	# 		setattr(self, key, kwargs[key])

	#todo: current initializate unelegant
	def __init__(self, hand=None, blackjack = 0, win = 0, split =0, double = 0, hitState =0, dealerHand = [], dealerScore = 0, score =0, originalScore =0, timestamp = ""):
		if hand is None:
			hand = []
		self.hand = hand
		#todo: re-add datetime once mDB implemented. Currently, won't work with lambda dict collapse
		#self.startTime = datetime.now(tz=None)
		self.blackjack = blackjack
		self.win = win
		self.split = split
		self.double = double
		self.hitState = hitState # 0 if stand, 1 if hit
		self.dealerHand = dealerHand
		self.dealerScore = dealerScore
		self.score = score
		self.originalScore = originalScore
		self.timestamp = timestamp

	def newHand(self,deck):
		self.hand.clear()
		self.blackjack = 0
		self.win = 0
		self.double = 0
		self.state = 0
		self.deal(deck)

	def deal(self, deck):
		for i in range(2):
			self.hand.append( deck.pop() )
		self.originalScore = self.total() #todo: testing if score function works

	#function to see if a split is possible. Assumes new hand (only 2 elements)
	def splitCheck(self):
		if len(self.hand) != 2:
			print("Hand not appropriate for a splitCheck()")
			return False
		if self.hand[0].value == self.hand[1].value:
			return True
		return False

	def __str__(self):
		handStr = str(self.hand[0])
		for card in self.hand[1:]:
			handStr = handStr + ", " + str(card)
		return handStr

	def total(self):
		total = 0
		for card in self.hand:
			card = card.value
			if card in [11, 12, 13]:
				total += 10
			elif card == 14:
				if total >= 11:
					total += 1
				else:
					total += 11
			else:
				total += int(card)
		return total

	def hit(self, deck):
		card = deck.pop()
		self.hand.append(card)

class Deck:
	def __init__(self, deckCount):
		dSuit = ["C","H","S","D"]  * 13 * deckCount
		dValue = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4 * deckCount
		self.cards = []
		for i in range(52*deckCount):
			self.cards.append( Card(dSuit.pop(),dValue.pop()) )

	def shuffle(self):
		random.shuffle(self.cards)

	def peek(self, number):
		for i in range(number):
			print(self.cards[-1*i])

	def pop(self):
		return self.cards.pop()

class Player:
	def __init__(self, name, cookie = "1", money = 1000, hands=None, currentHand=None):
		if hands is None:
			hands = []
		if currentHand is None:
			currentHand = [Hand()]
		self.name = name
		self.cookie = cookie
		self.money = money
		self.hands = hands
		self.currentHand = currentHand #will be array of hands, starts with 1 due to needing to access element 0

	#handIndex assumes moving through currentHand index in ascending order
	def split(self, handIndex,deck):
		#ends the function if handIndex throws an error
		if handIndex == -1:
			return
		self.currentHand.insert(handIndex+1, Hand())
		#adds last card in currentHand point, to new empty hand
		self.currentHand[handIndex+1].hand.append( self.currentHand[handIndex].hand.pop() )
		#adds new card to each hand
		for i in range(handIndex,handIndex++2):
			self.currentHand[i].hit(deck)
			self.currentHand[i].split = 1
			self.currentHand[i].originalScore = self.currentHand[i].total() #todo: testing if this works, score is in diff library

	def splitLogic(self, deck):
		#TODO HANDLE BLACKJACK FOR SPLITS
		i = 0
		while i < len(self.currentHand):
			if self.currentHand[i].splitCheck():
				clear()
				choice = input("[Y/N] Would you like to Split this hand?: \n" + str(self.currentHand[i]) + "\n").lower()
				if choice == "y":
					self.split( i,deck)
					print("New hands for " + self.name + ":")
					print( self.currentHand[i])
					print( self.currentHand[i+1])
					time.sleep(1)
				else:
					i += 1
			else:
				i += 1