import TestData.HandData as testData
import unittest
from bjObjects import *

#class TestHand(TestCase):
class TestHand(unittest.TestCase):
    
    def test_newHand(self):
        testHand = Hand()
        self.assertIsNotNone(testHand,"Fails if new hand not generated")

    def test_deal(self):
        testHand = Hand()
        tDeck = Deck(2)
        testHand.deal(tDeck)
        self.assertEqual( len(testHand.hand) , 2, "Passed if new hand has 2 cards")

    def test_splitCheck(self):
        testHandPass = Hand()
        testHandPass.hand = [Card("H", 7), Card("D", 7)]
        self.assertTrue(testHandPass.splitCheck(), "Fails if testHand1 is not eligible to split")

        testHandFail = Hand()
        testHandFail.hand = [Card("H", 6), Card("H", 8)]
        self.assertFalse(testHandFail.splitCheck(), "Passes if testHand1 is not eligible to split")

    def test_total(self):
        i = 0
        for hand in testData.testHands:
            i += 1
            tHand = Hand()
            for card in hand[0]:
                tHand.hand.append(card)
            self.assertEqual( tHand.total(), hand[1], "test case #" + str(i) + " was not equal to expected output")

    def test_hit(self):
        testHand = Hand()
        tDeck = Deck(2)
        testHand.deal(tDeck)
        testHand.hit(tDeck)
        self.assertEqual(len(testHand.hand), 3, "Fails if after 1 hit there aren't 3 cards")

if __name__ == '__main__':
    unittest.main()
