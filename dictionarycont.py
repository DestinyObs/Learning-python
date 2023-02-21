aliiens = []
for alien_number in range(30):
    new_alien = {'color': 'blue', 'speed': 'slow', 'points': 5}
    aliiens.append(new_alien)

for alien in aliiens[:3]:
    if alien['color'] == 'blue':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'superfast'
    else:
        alien['color'] = 'brown'
        alien['points'] = 10
        alien['speed'] = 'superfast'
    

for alien in aliiens[:6]:
    print(alien)

print (f"total number of aliens is: {len(aliiens)}")



pizza ={
    'crust':'thrist',
    'toppings': ['extra cream', 'mushroom']
}

print(f"you hvae ordered a {pizza['crust']}-crust pizza with the following:")
for topping in pizza['toppings']:
#blackslash t is fir the tab extension 
    print(f"\t{topping}")

#dictionary inside of dictionary

user = {
    'aeinstein': {
        'first': 'albert',
        'last':  'destiny',
        'location': ' prince line',
    },

    'macurie': {
        'first': 'destiny',
        'last': 'obueh',
        'location': 'paris',
    },
}

for username, user_info in user.items():
    print(f"\n Username: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\t Full Name: {full_name.title()}")
    print(f"\t Location: {location.title()}")