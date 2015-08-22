class Character:
	def __init__(self, h, d):
		self.health = h
		self.damage = d
		self.armor = []
	
	def add_armor(self, armor):
		self.armor.append(armor)
		
	def attack(self, other):
		for armor in self.armor:
			self.health += 25
		for armor in other.armor:
			other.health += 25
		if self.damage > other.health:
			print 'Player wins'
		elif enemy.damage > self.health:
			print 'Player loses'
		else:
			print 'Stalemate!'
			
player = Character(50, 300)
enemy = Character(250, 200)
enemy.add_armor('Laser Armor')
# fight!
player.attack(enemy)
