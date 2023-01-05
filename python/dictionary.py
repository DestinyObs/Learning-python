
# dictionary uses curly braces unlike list that used parethesis
alien_0 = {'color': 'blue', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"you have earned {new_points} points!")

# all you need to do is slestect the name then the key
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

# list are sorted and idctionaries are in abituary order 

alien_1 = {}

alien_1['color'] = 'blue'
alien_1['happy'] = 'happy'

print(f"the alien is {alien_1['happy']}")
alien_1['point'] = 100
alien_1['married'] = 'no'

print(alien_1) 

alien_0 = {'x_position': 0, 'x_position': 3.56, 'speed': 'fast'}
print(f"Original Position: {alien_0['x_position']} meters from y.")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'fast':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")


