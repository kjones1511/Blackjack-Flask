import unittest
import States
import json

tPath = '/Users/kjones/PycharmProjects/Blackjack4/Test/TestData/TestStateObjects.json'
tJSON = {}
with open(tPath) as file:
	tJSON =json.load(file)


class TestStates(unittest.TestCase):

	#todo: temp data test
	def test_FlaskReturn(self):
		# with open(tPath) as tJSON:
		# 	dictionary = json.load(tJSON)
		# 	print(dictionary['test1'])
		print(tJSON['test1'])

	#for later
	def signIn(self):
		return

	#Won't do anything initially, but need to plan for making tables for multiple games happening concurrently
	def launchTable(self):
		return

	def test_startHand(self):
		self.fail()


if __name__ == '__main__':
	unittest.main()
