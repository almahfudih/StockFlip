from collections import defaultdict
import json

class Portfolio():
	def __init__(self, username):
		if self.load_user(username) is None:
			self.owned_stocks = {}
			self.username = username
			self.credits = 0


	'''
	Set the stock to [quantity] at key value [symbol], independent of previous value
	Returns True on success, else False
	'''
	def set_stock(self, symbol, quantity):
		try:
			self.owned_stocks[symbol] = quantity
		except KeyError as e:
			raise e
			print("KeyErrorL " + e)
			return False

		assert self.owned_stocks[symbol] >= 0
		return True


	'''
	Set the quantity of owned stock equal to the old quantity + [quantity] at key [symbol]
	Returns True if successful, else False
	'''
	def add_stock(self, symbol, quantity):
		if not (isinstance(symbol, str) and (isinstance(quantity, int))):
			return False
		try:
			self.owned_stocks[symbol] += quantity
		except KeyError as e:
			raise e
			print("KeyError: " + e)
			return False
		assert self.owned_stocks[symbol] >= 0
		return True


	'''
	Set the quantity of owned stock equal to the old quantity - [quantity] at key [symbol]
	Returns True if successful, else False
	'''
	def remove_stock(self, symbol, quantity):
		self.owned_stocks[symbol] -= quantity

		assert owned_stocks[symbol] >= 0

	'''
	Display all __dict__ fields to display (self) object
	'''
	def print_portfolio(self):
		print(self.__dict__)


	'''
	Load a user using the username as the file, in JSON format into this object.
	Return true if loaded
		   false if None
	'''
	def load_user(self, username):
		with open(username + ".json", "r") as read_file:
			self.__dict__ = json.load(read_file)
		if self.__dict__ is not None:
			return True
		else:
			return False 


	'''
	Serialize (self) object and dump it into a file with self.username as the filename
	'''
	def dump_user_data(self):
		with open(self.username + ".json", "w") as write_file:
			json.dump(self.__dict__, write_file)


newUser = Portfolio("Brad")
newUser.add_stock("GOOGL", 88)

newUser.add_stock("GOOGL", 88)

#newUser.dump_user_data()

newUser.print_portfolio()