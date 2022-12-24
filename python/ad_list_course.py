magicians = ['Destiny','omo','obs']
for person in magicians:
    print(f"{person.title()} That has a great trick")
    print(f"I can't wait for another trick bro, {person.title()}.\n")
    
print("Thank you everyone it was an amazing trick")

Pizzas = {'mack','donalds','drizzy'}
for pizza in Pizzas:
    print(f"I love eating {pizza.title()} pizza \n")
    
print("i really love pizza")

animals = ['lion','dog','cat']
for animal in animals:
    print(f"{animal} love to eat food")
print("any one will make a great pet")


#list of number 

for value in list(range(1,11)):
    print(value)

#even_Numbers
numbers = list(range(2, 11, 2))
print(numbers)

#square of numbers 1-10
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)
#more simplified

squares = [value ** 2 for value in range(1,10)]
print(squares)


#min and max of range of values
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(max(digits))
print(min(digits))


#count 1-1milli

numbers = list(range(1,1000001))
print(min(numbers))
print(max(numbers))

print(sum(numbers))

for num in list(range(1, 21, 2)):
    print(num)

cubes = [value ** 3 for value in range(1, 11)]
for value in cubes:
    print(value)

numbers1 = list(range(3, 31, 3))
for n in numbers1:
    print(n)

#slicing
players = ['mummy','daddy','sisters','uncle','brother']

for player in players[:3]:
    print(player.title())

my_food = ['pizza','akpu','foody']
print(my_food)

friend_food = my_food[:]
my_food.append('fufu')
friend_food.append('ice_cream')

print(f"my fav food are \n {my_food}")
print(f"my friends fav food are \n {friend_food}")

listly = ['one','two','three']
for p in listly:
    print(f"{p}")

dimensions = (200, 50)

for dimension in dimensions:
    print(dimension)

dimensions = (400, 500)

print("\n Modified Dimension:")
for dimension in dimensions:
    print(dimension)

Food_we_eat = ('fufu','semo','eba','soups')
for food in Food_we_eat:
    print(food)
 

Food_we_eat = ('water','cake','semo','soups')
for food in Food_we_eat:
    print(food)