import random 
class board:
	def __init__(self): #creates a rectangle of walls stored in an array
		self.bord=[]
		self.data=[];
		for i in range(30):
			self.f=[]
			for j in range(80):
				self.f.append(" ")
			self.bord.append(self.f)
		for i in range(30):
			self.bord[i][0]='X'
			self.bord[i][79]='X'
		for i in range(80):
			self.bord[0][i]='X'
			self.bord[29][i]='X'
	#creates walls i.e. floors on random lenth and random side
	def createwall(self):
		self.hight=5
		for j in range(6):
			self.dt=[]
			self.wall=random.randrange(1,3)
			if self.wall==1:
				self.size=random.randrange(50,70)
				for i in range(self.size):
					self.bord[self.hight][i]='X'
				self.dt.append('l')
				self.dt.append(self.size-1)
			if self.wall==2:
				self.size=random.randrange(50,70)
				for i in range(self.size):
					self.bord[self.hight][79-i]='X'
				self.dt.append('r')
				self.dt.append(79-self.size)
			self.hight+=4
			self.data.append(self.dt)
		self.data.append(['l',77])

	#creates normal and broken ladders
	def createladder(self):
		self.hight=6
		lad=0
		i=0
		k=0
		brk=random.sample(range(0,5),3)
		brk=sorted(brk)
		while i<5:
			if self.data[i][0]=='r' and self.data[i+1][0]=='r':
				t=max(self.data[i][1],self.data[i+1][1])
				lad=random.randrange(t+2,75)
				while self.bord[self.hight][lad+1]=='H' or self.bord[self.hight][lad-1]=='H':
					lad=random.randrange(t+5,75)
				self.bord[self.hight-1][lad]=self.bord[self.hight][lad]=self.bord[self.hight+1][lad]=self.bord[self.hight+2][lad]='H'

			if self.data[i][0]=='l' and self.data[i+1][0]=='l':
				t=min(self.data[i][1]+2,self.data[i+1][1]-2)
				lad=random.randrange(5,t-2)
				while self.bord[self.hight][lad+1]=='H' or self.bord[self.hight][lad-1]=='H':
					lad=random.randrange(5,t-2)
				self.bord[self.hight-1][lad]=self.bord[self.hight][lad]=self.bord[self.hight+1][lad]=self.bord[self.hight+2][lad]='H'

			if self.data[i][0]=='r' and self.data[i+1][0]=='l':
				lad=random.randrange(self.data[i][1]+2,self.data[i+1][1]-2)
				while self.bord[self.hight][lad+1]=='H' or self.bord[self.hight][lad-1]=='H':
					lad=random.randrange(self.data[i][1]+2,self.data[i+1][1]-2)
				self.bord[self.hight-1][lad]=self.bord[self.hight][lad]=self.bord[self.hight+1][lad]=self.bord[self.hight+2][lad]='H'

			if self.data[i][0]=='l' and self.data[i+1][0]=='r':
				lad=random.randrange(self.data[i+1][1]+2,self.data[i][1]-2)
				while self.bord[self.hight][lad+1]=='H' or self.bord[self.hight][lad-1]=='H':
					lad=random.randrange(self.data[i+1][1]+2,self.data[i][1]-2)
				self.bord[self.hight-1][lad]=self.bord[self.hight][lad]=self.bord[self.hight+1][lad]=self.bord[self.hight+2][lad]='H'
			if i in brk:
				p=random.randrange(0,3)
				self.bord[self.hight+p][lad]=" "
				del brk[0]
			else:
				i+=1
				self.hight+=4
		if self.data[5][0]=='l':
			lad=random.randrange(3,self.data[5][1]-2)
			self.bord[self.hight-1][lad]=self.bord[self.hight][lad]=self.bord[self.hight+1][lad]=self.bord[self.hight+2][lad]='H'

		if self.data[5][0]=='r':
			lad=random.randrange(self.data[5][1]+2,75)
			self.bord[self.hight-1][lad]=self.bord[self.hight][lad]=self.bord[self.hight+1][lad]=self.bord[self.hight+2][lad]='H'

	# Creates coins at random positions on floor 
	def coin(self):
		self.hight=4
		for i in range(7):
			cns=[]
			if self.data[i][0]=='l':				
				cns=random.sample(range(2,self.data[i][1]-2),5)
			else:
				cns=random.sample(range(self.data[i][1]+2,77),5)
			for j in cns:
				if not self.bord[self.hight][j]=='H':
					self.bord[self.hight][j]='C'
			self.hight+=4
	#creates queen on the top according on which side the top floor is
	def queen(self):
		self.hight=2
		if self.data[0][0]=='l':
			self.bord[self.hight-1][14]='Q'
			for i in range(10):
				self.bord[self.hight][i+10]='X'
			self.bord[self.hight-1][10]=self.bord[self.hight-1][19]='X'
			self.bord[self.hight][16]=self.bord[self.hight+1][16]=self.bord[self.hight+2][16]='H'
		else:
			self.bord[self.hight-1][66]='Q'
		  	for i in range(10):
				self.bord[self.hight][i+60]='X'
			self.bord[self.hight-1][60]=self.bord[self.hight-1][69]='X'
			self.bord[self.hight][64]=self.bord[self.hight+1][64]=self.bord[self.hight+2][64]='H'

