# set up characters
player = {'health': 50, 'damage': 300, 'armor': []}
enemy = {'health': 250, 'damage': 200, 'armor': ['Laser Armor']}

# consume armor
for armor in enemy['armor']:
	enemy['health'] += 25
for armor in player['armor']:
	player['health'] += 25
	
# fight!
if player['damage'] > enemy['health']:
	print "player wins!"
elif enemy['damage'] > player['health']:
	print "player loses!"
else:
	print "stalemate!"