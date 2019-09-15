
class car():
	def __init__(self, price, color):
		self.price=price
		self.color=color

honda=car(1000000,'red')
tata=car(900000,'white')

honda.cc = 1500
print(honda.price)

print(honda.__dict__)

print(tata.__dict__)
