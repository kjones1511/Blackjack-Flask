import TestData.cardData as testData
import unittest
from ConsoleGameFunctions import *
#test array
# for test_str, checks that the card object prints the string in 2nd element of array pairs
# for test_equal, compares pairs of initial array elements for equality

testCards = testData.testCards

class TestCard(unittest.TestCase):
    #counts number of matching cards, if greater than 45 assuming deck didn't shuffle
    def test_init(self):
        testCard = Card("H", 7)
        self.assertIsNotNone(testCard,"Fails if new card not generated")

    def test_str(self):
        for card in testCards:
            self.assertEqual(str(card[0]),card[1],"failed to print card correctly")

    def test_equal(self):
        self.assertEqual( Card("H", 7), Card("H", 7), "Cards are not equal")
        self.assertEqual( Card("C", 11), Card("C", 11), "Cards are not equal")
        self.assertEqual( Card("D", 14), Card("D", 14), "Cards are not equal")
        self.assertNotEqual( Card("S", 14), Card("S", 12), "Cards should not be equal")
        self.assertNotEqual( Card("C", 12), Card("S", 12), "Cards should not be equal")

if __name__ == '__main__':
    unittest.main()
