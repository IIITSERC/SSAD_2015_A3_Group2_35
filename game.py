import pygame
import random
import q
import w
import e
import time

clock=pygame.time.Clock()
b=w.board()
r=q.Player()
dnk=q.Donkey()
fb=e.fireball()
pygame.init()
gameDisplay=pygame.display.set_mode((1200,700))
gameExit=False
text=pygame.font.SysFont(None,25)
img1=pygame.image.load("live.png")
lve=pygame.transform.scale(img1,(40,40))
img2=pygame.image.load("wall.png")
wal=pygame.transform.scale(img2,(15,20))
img3=pygame.image.load("H.png")
ladr=pygame.transform.scale(img3,(15,20))
img4=pygame.image.load("lft.png")
pl=pygame.transform.scale(img4,(20,20))
img5=pygame.image.load("rit.png")
pr=pygame.transform.scale(img5,(20,20))
img6=pygame.image.load("coin.png")
cn=pygame.transform.scale(img6,(20,20))
img7=pygame.image.load("ball.png")
bl=pygame.transform.scale(img7,(15,20))
img8=pygame.image.load("prnc.png")
princ=pygame.transform.scale(img8,(15,20))
img9=pygame.image.load("donk.png")
monk=pygame.transform.scale(img9,(15,20))
img11=pygame.image.load("lost.png")
lost=pygame.transform.scale(img11,(400,450))
img12=pygame.image.load("over.png")
over=pygame.transform.scale(img12,(1173,268))
x=0
y=0
b.createwall()
b.createladder()
b.queen()
b.coin()
key=0
l=0
location=[]

#Donkey position updating
if b.bord[5][1]!='X':
	key=1
	dnk.dx=4
	dnk.dy=78
#Checking player collision with fireball 
def checkcollision():
	if fb.ball[r.xx][r.yy]=="O":
		r.xx=28
		r.yy=2
		r.lives-=1
		r.score-=25
		if r.lives==0:
			gameDisplay.fill((0,0,0))
			gameDisplay.blit(over,(10,200))
			pygame.display.update()
			time.sleep(1)
			pygame.quit()
			quit()
		else:
			gameDisplay.fill((0,0,0))
			gameDisplay.blit(lost,(400,150))
			pygame.display.update()
			time.sleep(1)	
#Checking for completion of present level
def checkgamecomplete():
	if b.bord[r.xx][r.yy]=='Q':
		r.score+=50
		r.xx=28
		r.yy=2
		fb.__init__()
		dnk.__init__()
		b.__init__()
		b.createwall()
		b.createladder()
		b.queen()
		b.coin()
		global key,state,ky,ui,ub,uc,l,location,ls
		location=[]
		key=0
		state=1
		ky=key
		collectcoin(28,2)
		ui=0
		ub=-1
		uc=-1
		l=0
		ls=[]
		if b.bord[5][1]!='X':
			key=1
			dnk.dx=4
			dnk.dy=78
		
#Refreshing and updating display
def update():
	global l
	checkcollision()
	checkgamecomplete()
	gameDisplay.fill((0,0,0))
	y=0
	for i in range(30):
		x=0
		for j in range(80):
			if b.bord[i][j]=='X':
				gameDisplay.blit(wal,(x,y))
			elif b.bord[i][j]=='H':
				gameDisplay.blit(ladr,(x,y))			
			elif b.bord[i][j]=='C':
				gameDisplay.blit(cn,(x,y))
			elif b.bord[i][j]=='Q':
				gameDisplay.blit(princ,[x,y])
			if fb.ball[i][j]=="O":
				gameDisplay.blit(bl,(x,y))
			x=x+15
		y=y+20
	pts=text.render("Your Score "+str(r.score),True,(255,255,255))
	gameDisplay.blit(pts,[500,650])
	lip=800
	for i in range(r.lives):
		gameDisplay.blit(lve,(lip,650))
		lip+=40
	if l==0:
		gameDisplay.blit(pr,[r.yy*15,r.xx*20])	
	else:
		gameDisplay.blit(pl,[r.yy*15,r.xx*20])	

	gameDisplay.blit(monk,[dnk.dy*15,dnk.dx*20])
	pygame.display.update()
	clock.tick(20)			

update()
state=1

#Collecting coins if the player position is same as coin position
def collectcoin(z,c):
	if b.bord[z][c]=='C':
		b.bord[z][c]=" "
		r.score+=5
collectcoin(28,2)
ui=0
ub=-1
uc=-1
l=0
ls=[]
ky=key

#Creating fireballs from donkey
def createfireball():
	fb.ball[dnk.dx][dnk.dy]='O'
	if ky==0:
		ls.append(['r',dnk.dx,dnk.dy])
	else:
		ls.append(['l',dnk.dx,dnk.dy])

#moving donkey and fireballs 
def donkeyfbmovement():
	global state
	global ui
	global ky
	ui+=1
	ui=ui%3
	if (key==0) and ui==0:
		if (dnk.dy<15) and state==1:
			dnk.dy+=1
			ky=0
			if (dnk.dy==15):
				state=0
				ky=1
		else:
			dnk.dy-=1
			ky=1
			if(dnk.dy==1):
				ky=0
				state=1
	if (key==1) and ui==0:
		if (dnk.dy<79 and state==1):
			dnk.dy-=1
			ky=1
			if (dnk.dy==65):
				 state=0
				 ky=0
		else:
			dnk.dy+=1
			ky=0
			if (dnk.dy==78):
				ky=1
				state=1
	lis=[]
	global uc
	uc+=1
	uc=uc%4
	if uc==0: 
		for i in range(len(ls)):
			if ls[i][1]==28 and ls[i][2]==3:
				lis.append(i)		
			else:
				if(ls[i][0]=='l'):
					if(ls[i][2]==1):
						ls[i][0]='r'
					elif(ls[i][2]==2):
						ls[i][0]='r'
						ls[i][2]-=1
						fb.ball[ls[i][1]][ls[i][2]+1]=" "
						fb.ball[ls[i][1]][ls[i][2]]="O"
				
				
					else:
						if (b.bord[ls[i][1]+1][ls[i][2]]=="H"):
							lo=random.randrange(0,2)
							if lo==1:
								ls[i][0]='h'
								fb.ball[ls[i][1]][ls[i][2]]=' '
								ls[i][1]+=1
								fb.ball[ls[i][1]][ls[i][2]]="O"
								ls[i][0]='h'
					
		
						if(b.bord[ls[i][1]+1][ls[i][2]-1] in ['X','H']) and ls[i][0]=='l':
							ls[i][2]-=1
							fb.ball[ls[i][1]][ls[i][2]+1]=" "
							fb.ball[ls[i][1]][ls[i][2]]="O"
						elif (b.bord[ls[i][1]+1][ls[i][2]-1])==" " and ls[i][0]=='l':
							ls[i][0]='h'
							ls[i][2]-=1
							fb.ball[ls[i][1]][ls[i][2]+1]=" "
							fb.ball[ls[i][1]][ls[i][2]]="O"
	
			
				elif(ls[i][0]=='r'):
					if ls[i][2]==78:
						ls[i][0]='l'
					elif ls[i][2]==77:
						ls[i][0]='l'
						ls[i][2]+=1
						fb.ball[ls[i][1]][ls[i][2]-1]=" "
						fb.ball[ls[i][1]][ls[i][2]]="O"
					else:
						if (b.bord[ls[i][1]+1][ls[i][2]])=='H':
							lo=random.randrange(0,2)
							if lo==1:
								ls[i][0]='h'
								fb.ball[ls[i][1]][ls[i][2]]=" "
								ls[i][1]+=1
								fb.ball[ls[i][1]][ls[i][2]]=" "
	
						if b.bord[ls[i][1]+1][ls[i][2]+1] in ['X','H'] and ls[i][0]=='r':
							ls[i][2]+=1
							fb.ball[ls[i][1]][ls[i][2]-1]=" "
							fb.ball[ls[i][1]][ls[i][2]]="O"
						elif (b.bord[ls[i][1]+1][ls[i][2]+1])==" " and ls[i][0]=='r':
							ls[i][2]+=1
							ls[i][0]='h'
							fb.ball[ls[i][1]][ls[i][2]-1]=" "
							fb.ball[ls[i][1]][ls[i][2]]="O"
	

				if ls[i][0]=='h':
					if(b.bord[ls[i][1]+1][ls[i][2]])=='X':
						lo=random.randrange(0,2)
						if lo==1:
							ls[i][0]='l'
						else:
							ls[i][0]='r'
			
					elif (b.bord[ls[i][1]+1][ls[i][2]]=='H' and b.bord[ls[i][1]+1][ls[i][2]+1]=='X'):
						lo=random.randrange(0,3)
						if lo==1:
							ls[i][0]='l'
						if lo==2:
							ls[i][0]='r'
						else:
							ls[i][0]='h'
					else:
						fb.ball[ls[i][1]][ls[i][2]]=" "
						fb.ball[ls[i][1]+1][ls[i][2]]="O"
						ls[i][1]+=1
				
		
		for i in lis:
			del ls[i]
		fb.ball[28][3]=" "
	global ub
	ub+=1
	ub=ub%50
	if (ub==0):
		createfireball()

#Main game loop		
while not gameExit and r.lives>0:
	
	donkeyfbmovement()
	update()
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			gameExit=True
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_q:
				gameExit=True
	

	if pygame.key.get_pressed()[pygame.K_a] !=0 and b.bord[r.xx][r.yy-1]!='X':

		if b.bord[r.xx+1][r.yy-1] in ['X','H']:

			if b.bord[r.xx][r.yy-1]=='H' and b.bord[r.xx-1][r.yy]=='H' and b.bord[r.xx+1][r.yy]=='H':
				pass

			else:
				r.yy-=1
				l=1
				collectcoin(r.xx,r.yy)
				donkeyfbmovement()
				update()

		elif b.bord[r.xx+1][r.yy] =='X' and b.bord[r.xx+1][r.yy-1]==" ":
			r.yy-=1
			l=1	
			while (b.bord[r.xx+1][r.yy]!='X'):
				r.xx+=1

				collectcoin(r.xx,r.yy)
				donkeyfbmovement()
				update()
				
	elif pygame.key.get_pressed()[pygame.K_d]!=0 and b.bord[r.xx][r.yy+1]!='X':

		if b.bord[r.xx+1][r.yy+1] in ['X','H']:

			if b.bord[r.xx][r.yy+1]=='H' and b.bord[r.xx-1][r.yy]=='H' and b.bord[r.xx+1][r.yy]=='H':
				pass
			
			else:
				l=0
				r.yy+=1
				collectcoin(r.xx,r.yy)
				donkeyfbmovement()
				update()

		elif b.bord[r.xx+1][r.yy] =='X' and b.bord[r.xx+1][r.yy+1]==" ":
			r.yy+=1
			l=0
			while(b.bord[r.xx+1][r.yy] != 'X'):
				r.xx+=1
				collectcoin(r.xx,r.yy)
				donkeyfbmovement()
				update()

	elif pygame.key.get_pressed()[pygame.K_w]!=0 and b.bord[r.xx][r.yy]=='H':

		r.xx-=1
		collectcoin(r.xx,r.yy)
		donkeyfbmovement()
		update()

	elif pygame.key.get_pressed()[pygame.K_s]!=0 and b.bord[r.xx+1][r.yy]=='H':
		r.xx+=1
		donkeyfbmovement()
		update()
	elif pygame.key.get_pressed()[pygame.K_SPACE]:
		tmp=r.xx
		if l==0 and (b.bord[r.xx+1][r.yy+1] == 'X' or b.bord[r.xx+1][r.yy]=='X'):
			r.yy+=2
			r.xx-=1
			if r.yy<79:
				collectcoin(r.xx,r.yy)
				donkeyfbmovement()
				update()
				r.yy+=2
				r.xx-=1
				if r.yy<79:
					donkeyfbmovement()
					update()
					collectcoin(r.xx,r.yy)
					r.yy+=2
					r.xx+=1
					if r.yy<79:
						donkeyfbmovement()
						collectcoin(r.xx,r.yy)
						update()
						r.yy+=2
						r.xx+=1
						if r.yy<79:
							collectcoin(r.xx,r.yy)
							donkeyfbmovement()
							update()
						else:
							r.yy=78
							r.xx=tmp
							collectcoin(r.xx,r.yy)
							donkeyfbmovement()
							update()
					else:
						r.yy=78
						r.xx=tmp
						collectcoin(r.xx,r.yy)
						donkeyfbmovement()
						update()
				else:
					r.yy=78
					r.xx=tmp
					collectcoin(r.xx,r.yy)
					donkeyfbmovement()
					update()
			else:
				r.yy=78
				r.xx=tmp
				collectcoin(r.xx,r.yy)
				donkeyfbmovement()
				update()

			if b.bord[r.xx+1][r.yy]==" ":
				while(b.bord[r.xx+1][r.yy] != 'X'):
					r.xx+=1
					collectcoin(r.xx,r.yy)
					donkeyfbmovement()
					update()
			collectcoin(r.xx,r.yy)
		elif l==1 and( b.bord[r.xx+1][r.yy-1] =='X' or b.bord[r.xx+1][r.yy]=='X'):	
			r.yy-=2
			r.xx-=1
			if r.yy>0:
				collectcoin(r.xx,r.yy)
				donkeyfbmovement()
				update()
				r.yy-=2
				r.xx-=1
				if r.yy>0:
					collectcoin(r.xx,r.yy)
					donkeyfbmovement()
					update()
					r.yy-=2
					r.xx+=1
					if r.yy>0:
						collectcoin(r.xx,r.yy)
						donkeyfbmovement()
						update()
						r.yy-=2
						r.xx+=1
						if r.yy>0:
							collectcoin(r.xx,r.yy)
							donkeyfbmovement()
							update()
						else:
							r.yy=1
							r.xx=tmp
							collectcoin(r.xx,r.yy)
							donkeyfbmovement()
							update()
					else:
						r.yy=1
						r.xx=tmp
						collectcoin(r.xx,r.yy)
						donkeyfbmovement()
						update()
				else:
					r.yy=1
					r.xx=tmp
					collectcoin(r.xx,r.yy)
					donkeyfbmovement()
					update()
			else:
				r.yy=1
				r.xx=tmp
				collectcoin(r.xx,r.yy)
				donkeyfbmovement()
				update()
			if b.bord[r.xx+1][r.yy]==" ":
				while(b.bord[r.xx+1][r.yy] != 'X'):
					r.xx+=1
					collectcoin(r.xx,r.yy)
					donkeyfbmovement()
					update()
			collectcoin(r.xx,r.yy)
pygame.display.update()
pygame.quit()
quit()
