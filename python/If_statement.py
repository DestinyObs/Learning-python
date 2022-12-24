cars = ['bmw','subaru','toyota','ford']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


x = 20
y = 5

if x == 20:
    print((x+y)*y)

car = 'audi'
print(car != 'bmw') #equality operation for comparison

available_toppings =['moimoi','flakes','soaks','sugar','butter']
requested_toppings = ['mushroom','moimoi','french fries']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"We are adding the requested toppings {requested_topping}")
    else:
        print(f"So Sorry. we don't have {requested_topping} anymore ")

print("\n Finished making your pizza ")

User_names = ['admin','destiny','obueh','dami']

if User_names:
    for username in User_names:
        if username == 'admin':
            print(f"Hello {username.upper()}, Would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you very logging in again")
else:
    print("We need to find some users!!!")

current_user =['admin','destiny','obueh','dami']
new_users = ['john','destiny','eme','Dami']

for new_user in new_users:
    if new_user.lower() in current_user:
        print(f"Hello Username {new_user.title()} already in use")
    else:
        print(f"this username {new_user.title()} is available")
    


requested_topping = ['garri']

if requested_topping:
    for requested_toppings in requested_topping:
        if requested_toppings == 'onions':
            print("sorry we are out of onions")
        else:
            print(f"adding {requested_toppings.title()}")
        
    print("\n Finished With your food")
else:
    print("are you sure you want a pizza")

if 'mushroom' not in requested_topping:
    print("have fun eating.... i wont join you")
else:
    print("great let's it")


if requested_topping != 'meme':
    print("Hold your horses")
else:
    print("continue cooking")

age = 16
if age >= 18:
    print("Bro Step into that place ya fully of age")
else:
    print("sorry lad we can't get momma angry step back home son")

age_0 = 19
age_1 = 24

print(age_0 <= 20 and age_1 >=25)

banned_user = ['peter','paul','john','solomon']
user = 'mary'

if user not in banned_user:
    print(f"{user.title()}, you are not in the list of banned users")\

car = 'subaru'
print("Is car == 'subaru'? i predict True")

print(car == 'subaru')

age = 19
if age >= 18:
    print("You're ")
    print("You're old")
    print("You're old enough ")
    print("You're old enough to")
    print("You're old enough to vote!")
else:
    print("werey step!!!")

age = 50
if age <4:
    price = 0
if age < 18:
    price = 25
if age < 65:
    price = 40
if age >= 65:
    price = 20

print(f"Your mouney is ${price}")

Alien_color = ['green','yellow','red']

if 'green' in Alien_color:
    print("That player just eanred 5 points")
else:
    print("get out of here ")

alien_color = 'red'

if alien_color == 'green':
    print("You just earned 5 points")
elif alien_color == 'yellow':
    print("You just earned 10 points")
elif alien_color == 'red':
    print("You just earned 15 points")

age = 1
if age < 2:
    print("You are a baby")
elif (age >= 2 and age <4):
    print("you are a toodler")
elif age <13:
    print("you are a kid")
elif age <20:
    print("you are a teenager")
elif age <65:
    print("you are an adult")
elif age >=65:
    print("you are an elder")

fav_food = ['banna','grape','akpu','kiwi']

if 'kiwi' in fav_food:
    print(f"wow crazy you love {fav_food[3].title()}")
if 'grape' in fav_food:
    print(f"wow crazy you love {fav_food[1].title()}")
if 'akpu' in fav_food:
    print(f"wow crazy you love {fav_food[2].title()}")
if 'pine'  in fav_food:
    print("sorry we do not hhave it")
if 'banna' in fav_food:
    print(f"wow crazy you love {fav_food[0].title()}")


numbers = list(range(1, 100))

for number in numbers:
    if number == 1:
        print(f"{number}st \n")
    elif number == 2:
        print(f"{number}nd \n")
    elif number == 3:
        print(f"{number}rd \n")
    else:
        print(f"{number}th \n")