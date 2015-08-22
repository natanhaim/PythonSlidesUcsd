class MyPlayer:
	game = 'Mortal Wombat'
	def __init__(self, H):
		self.health = H
		self.powerups = 0
	def add_powerup(self):
		self.powerups += 1
	def print_state(self):
		print self.game, self.health, self.powerups
		
left_player = MyPlayer(100)
right_player = MyPlayer(50)
left_player.add_powerup()
left_player.print_state()
right_player.print_state()