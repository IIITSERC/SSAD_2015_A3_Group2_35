	
class Person:
	def __init__(self):
		self.xx==29
		self.yy=2

#Player inherits from Person class
class Player(Person):
	def __init__(self):
		self.lives=3
		self.score=0
		self.xx=28
		self.yy=2
#Donkey inherits from Person class	
class Donkey(Person):
	def __init__(self):
		self.dx=4
		self.dy=1
