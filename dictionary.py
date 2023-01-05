
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
del alien_1['color']
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


favourite_P_lang = {
    'jen': 'python',
    'sandra': 'c++',
    'sarah': 'c#'
}
lang = favourite_P_lang['jen'].title()
print(f"Jen fav lang is {favourite_P_lang['jen'].title()}")

print(favourite_P_lang.get('jen', 'no such user.'))

person = {'first_name': 'peter','last_name': 'last_name', 'age': 80,'city': 'calicali'}

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

fav_num = {
    'peter': 7,
    'bob': 3,
    'logan': 9,
    'lisa': 6,
    'destiny': 29,
    'praise': 5,
}

print(f"peter's favourite number is {fav_num['peter']}.")
print(f"bob's favourite number is {fav_num['bob']}.")
print(f"logan's favourite number is {fav_num['logan']}.")
print(f"lisa's favourite number is {fav_num['lisa']}.")
print(f"destiny's favourite number is {fav_num['destiny']}.")
print(f"praise's favourite number is {fav_num['praise']}.")

glosary = {
    'string': 'sequence of charcaters wrapped in quote',
    'boolean': 'choose if c=valuers are true or false',
    'list': 'mutable, ordered sequence of element',
    'tuples': 'immutable oredered ',
    'int': 'whole numbers',
}

#dictionary

for key, values in glosary.items():
    print(f"{key.title()}: {values}")
print(f"string is a {glosary['string']} \n")
print(f"boolean is a {glosary['boolean']} \n")
print(f"list is a {glosary['list']} \n")
print(f"tuples is a {glosary['tuples']}\n")

# lopping through dictionaries

user_me = {
    'username': 'efemo',
    'first': 'internet',
    'last': 'femo',
}

for key, value in user_me.items():
    print(f"key: {key}")
    print(f"value: {value} \n")


favourite_P_lang = {
    'jen': 'python',
    'sandra': 'c++',
    'sarah': 'c#',
    'dayo': 'java',
    'obueh': 'java',    
}

people = ['jen', 'paul', 'edwards']

for person in people:
    if person in favourite_P_lang.keys():
        print(f"Hey, {person.title()}, thank you for taking the poll")
    else:
        print(f"Hey, {person.title()}, please take the poll")

friends = ['jen', 'dayo']
for name, language in favourite_P_lang.items():
    print(f"{name.title()}'s fav lang is {language.title()}.\n")

for name in sorted(favourite_P_lang.keys()):
    print(f"{name.title()}, thank you for taking the poll check with us ")

for language in set(favourite_P_lang.values()):
    print(language.title())


for name in favourite_P_lang.keys():
    print(f"Hi {name.title()}\n")
    if name in friends:
        languages = favourite_P_lang[name].title()
        print(f"\t{name.title()}, i see you love {languages}")

for value in favourite_P_lang.values():
    print(value.title())


rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtse': 'china'
}

for river, country in rivers.items():
    print(f"the {river.title()} runs through {country.title()}")

print("\n")

for river in rivers.keys():
    print(river.title())

print("\n")

for country in rivers.values():
    print(country.title())

alien_2 = {'colo': 'green', 'point': '5'}
alien_3 = {'colo': 'red', 'point': '25'}
alien_4 = {'colo': 'blue', 'point': '54'}
alien_5 = {'colo': 'purple', 'point': '65'}
alien_6 = {'colo': 'magnet', 'point': '15'}

aliens = [alien_2, alien_3, alien_4, alien_5, alien_6]

for alien in aliens:
    print(alien)