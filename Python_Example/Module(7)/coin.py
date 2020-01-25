import random
class Coin:
	def __init__(self):
		self.sideup="Heads"
	def toss(self):
		if(random.randint(0,1))==1:
			self.sideup="Heads"
		else: self.sideup="Tails"
	def get_sideup(self):
		return self.sideup
def main():
	my_coin=Coin()
	print("This side is up: ",my_coin.get_sideup())
	print("Tossing the Coin")
	my_coin.toss()
	print("Now Side Up is: ",my_coin.get_sideup())
main()
