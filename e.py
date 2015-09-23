#creates a storage for fireballs
class fireball():
	def __init__(self):
		self.ball=[]
		for i in range(30):
			f=[]
			for i in range(80):
				f.append(" ")
			self.ball.append(f)

