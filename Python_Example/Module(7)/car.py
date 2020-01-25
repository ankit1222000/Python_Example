class Car:
	
	def __init__(self,colour,mileage):
		self.colour=colour
		self.mileage=mileage
	def __str__(self):
		return f'a {self.colour} car {self.mileage}'
car=Car("Red",10)
print(car)
