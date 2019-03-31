import random
class FairRoulette(): 
	def __init__(self):
		self.pockets=[]

		for i in range(1,37):
			self.pockets.append(i)
		self.ball=None
		self.pocketOdds = len(self.pockets) - 1 
	def spin(self): 
		self.ball = random.choice(self.pockets) 
	def betPocket(self, pocket, amt): 
		if str(pocket) == str(self.ball): 
			return amt*self.pocketOdds 
		else:
			return -amt  
	def __str__(self):
		return "me"+str(self.ball)

def play(game, numSpins, pocket, bet,toPrint):
	totPocket=0
	for i in range(numSpins):
		game.spin() 
		totPocket += game.betPocket(pocket, bet) 
	if toPrint: 
		print(numSpins, 'spins of', game) 
		print('Expected return betting', pocket, '=', str(100*totPocket/numSpins) + '%\n') 
	return (totPocket/numSpins)  


game = FairRoulette()  
for numSpins in (100, 1000000): 
	for i in range(3):
		play(game,numSpins,8,9,True)

