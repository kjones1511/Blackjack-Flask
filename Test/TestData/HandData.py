from bjObjects import *

testHands = [
	[[Card("H", 7), Card("D", 7)], 14],  # test matching values
	[[Card("H", 7), Card("D", 7), Card("D", 10)], 24],  # test bust
	[[Card("H", 3), Card("J", 4), Card("J", 4)], 11],  # test that 3+ cards can get scores
	[[Card("H", 2), Card("D", 10)], 12],  # series of tests on face values
	[[Card("S", 4), Card("D", 11)], 14],
	[[Card("H", 3), Card("D", 12)], 13],
	[[Card("H", 11), Card("D", 13)], 20],
	[[Card("H", 11), Card("D", 14)], 21],  # next few tests confirm Ace behavior
	[[Card("H", 4), Card("J", 14)], 15],
	[[Card("H", 6), Card("J", 6), Card("J", 14)], 13]
	# todo: test that 1 card shouldn't be scored alone [Card("J", 4)]
]

