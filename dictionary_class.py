Person_1 = {'first_name': ' Peter', 'last_name': 'Destiny', 'age': 19, 'city': 'nigeria'}
Person_2 = {'first_name': ' mary', 'last_name': 'eledu', 'age': 40, 'city': 'niger'}
Person_3 = {'first_name': ' bob', 'last_name': 'bobby', 'age': 34, 'city': 'Lagos'}


people = [Person_1, Person_2, Person_3]
print("\n")
for person in people:
    for k, v in person.items():
        print(f"{k}: {v}")
    print("\n")



pet_1 = {'animal': 'Dog', 'owner': 'DestinyO',}
pet_2 = {'animal': 'Cat', 'owner': 'DestinyOb',}
pet_3 = {'animal': 'Bird', 'owner': 'DestinyObs',}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"the pet is a {pet['animal']}. The Owner's name is {pet['owner'].title()}")

Fav_Places = {
    'peter': ['new york', 'london'],
    'Destiny': ['dubai', 'ameria'],
    'Dami': ['dubai', 'tokio'],
}

for name, place in Fav_Places.items():
    print(f"{name.title()}'s Favourite place are:")
    for place in place:
        print(f"\t {place.title()}")
    print("\n")

fav_num = {
    'peter': [7],
    'bob': [3, 5],
    'logan': [9],
    'lisa': [6, 9, 8, 7,],
    'destiny': [2, 0],
    'praise': [5],
}

for name, number in fav_num.items():
    print(f"{name.title()}'s favourite numbers are:")
    for num in number:
        print(f"\t {number}")
    print("\n")


cities = {
     'new york': {'country': 'united states', 'population': 8.4, 'fact': 'more than 800 languages spoken nationwide'},
     'london': {'country': 'united states', 'population': 9.4, 'fact': 'capital of the united kingdom'},
     'Uk': {'country': 'germany', 'population': 4.4, 'fact': 'seperated by the berlin wall'},

}

for city, details in cities.items():
    print(f"{city.title()} is located in {details['country']}, has a population of ~{details['population']} million.")
    print(f"fact about {city}: {details['fact']}\n")