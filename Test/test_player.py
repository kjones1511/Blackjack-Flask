import unittest
from bjObjects import *

#class TestHand(TestCase):
class TestPlayer(unittest.TestCase):
    #counts number of matching cards, if greater than 45 assuming deck didn't shuffle
    #assumes only testing for cases that pass Hand.splitcheck
    #todo: add test case for multiple hands in split
    def test_split(self):
        # list of test conditions
        tDeck = Deck(1)
        tPlayer = Player("temp", 1000)
        tPlayer.currentHand.append( Hand() )
        testHands = [
            [Card("H", 7), Card("D", 7)],  # normal split
            [Card("H", 12), Card("J", 12)],  # face split fit
        ]
        # testloop START
        for hand in testHands:
            #reset player values
            tPlayer.currentHand =  [ 1 ]
            tPlayer.currentHand[0] = Hand()
            #add test cards to hand
            for card in hand:
                tPlayer.currentHand[0].hand.append(card)
            #end if there aren't 2 hands after split
            tPlayer.split(0,tDeck)
            self.assertIs( len(tPlayer.currentHand), 2, "fails if there aren't 2 hands after split")


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

if __name__ == '__main__':
    unittest.main()
