# # user inputs and my code dixplays back 
message = input("Tell me somethnig i will repaeat back to you: ")
print(message)

name = input("Please Enter Your Name: ")
print(f"\nHello, {name}!")

prompt = "if you tell us who you are we can personalize your message"
prompt += "\n Please Enter Your Name: "

name = input(prompt)
print(f"Hello {name}")

name = input("What Is Your Name? ")
height = int(input(f"{name} How tall do you think you are in inches? "))

if height >= 48:
    print(f"You are tall enough to talk with me!")
else:
    print("\n All This Short people Sef, Why are you short!!! \n so short, dont worry when you are tall enough come back")
 
number = int(input("Enter a Number, it'd check if even or odd: "))

if number % 2 == 0:
    print(f"{number}, is even")
else:
    print(f"{number}, is odd")

Rental_Car = input("What Kind of rental Car would you like? ")
print(f"Let me see if i have a {Rental_Car}")

Resturant_seating = int(input("How many peopl are in thier dinner group? "))
if Resturant_seating > 8:
    print(f"Due to the excess amount of seaters i.e {Resturant_seating}, They'd have to wait for a table")
else:
    print(f"Oh {Resturant_seating}, That's perfect, your table is ready")

Numb = int(input("Gimmi a number? "))
if Numb % 10 != 0:
    print(f"{Numb}, is not a multiple of 10")
else:
    print(f"{Numb}, is a perfect multiple")

current_number = 1
while current_number <= 100:
    print(f"{current_number}")
    current_number += 10

promtply = "\n Tell me a number i'd repaeat for you, you can quit when you want to: "
promtply += "\n Enter 'quit' to end loop! "

active = True

while active:
    message = input(promtply)

    if message == 'quit':
        active = False
    else:
        print(message)

text = "marry me"

while text == 'marry me':
    print("I love you destiny")


prommpt = "\n Please enter the name of a city you have visited:"
prommpt += "\n Enter 'quit' when you have finished! "

while True:
    city = input(prommpt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")


number_count = 0

while number_count < 10:
    number_count += 1
    if number_count % 2 == 0:
        continue
    print(number_count)


x = 1
while x <= 5:
    print(x)
    x += 1


toppings = "\n Enter a series of toppings you'd want on your pizaa and we'd add it: "
toppings += "\n Enter 'quit' to end loop! "

while True:
    topping = input(toppings)

    if topping == 'quit':
          break
    else:
          print(f"We'd add {topping.title()} to your pizza")


prrompt = "\n How are are you there"
prrompt += "\n (Type 'quit' to stop the current excecution): "

active = True

while active:
    age = input(prrompt)
    
    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            price = 0
        elif age < 13:
            price = 10
        else:
            price = 15
        # else:
        #     print(f"{age} years old, will you get out of that place")
        print(f"The ticket price is ${price}")

#infinite loop
value = 5

while value < 10:
    print("Still Running")
    print("---")
 

unconfirmed_users = ['alice', 'bran', 'destiny', 'obs']
confirmed_users = []


while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"veryfying suer: {current_user.title()}")
    confirmed_users.append(current_user)

print("\n The following user have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


#program to remove multiple occurence of a value in our lsit

pets = ['dog', 'cats', 'cat', 'lion', 'goat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)

# collecting user response and storing it in a dictionary 
responses = {}
polling_active = True

while polling_active:
    name = input("\n What is your name? ")
    response = input("\n Which mountain would you like to climb someday? ")

    responses[name] = response

    repeat = input("\n Would you like to let another preson respond (yes/no)? ")
    if repeat == 'no':
        polling_active = False
    else:
        polling_active = True

print("\n ---Polling Results---")
for name, response in responses.items():
    print(f"\n {name}, Would you like to climb {response}.")

sandwich_orders = ['pastrami', 'chicken', 'pastrami', 'tuna', 'pastrami']
finished_sandwiches = []

print("Sorry we ran out of pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
     
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"\n I made your {sandwich} sandwich.")

    finished_sandwiches.append(sandwich)

print(f"\n ---Finished Sandwiches---")
for sandwich in finished_sandwiches:
    print(f"\n We made a {sandwich} sandwich!!!")



ressponses = {}
poolling_active = True

while poolling_active:
     name = input("What is your name? ")
     response = input("If you could visit a place in the world where will you go? ")

     ressponses[name] = response

     repeat = input("Would you like to let another preson respond (yes/no)? ")
     if repeat == 'no':
         poolling_active = False
     else:
         poolling_active = True


print("\n ---Polling Results---")
for name, response in ressponses.items():
    print(f"\n {name}, Would likw to visit Obs{response}.")