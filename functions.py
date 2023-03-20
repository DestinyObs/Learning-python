#def is used to define a function
#steps to define the functions are def then the function name e.g

def greet_user(username):
    """Display a simple greeting of love"""
    print(f"I love you, {username.title()}")

greet_user('Jesse')
greet_user('Destiny')
greet_user('Mary')
greet_user('Jesus')

#parameters deifined inside our functions and arguement deifined outside 
#Parameter is the variable listed insdie the parenteses in the function definition.
#Argument is the value sent to the function when it's called 


def Display_Message():
    """Display a simple Message"""
    print(f"\n Hola! We are Learning fuctions in the module")

Display_Message()

def Book_title(name_of_book):
    """Accepts the book title and print the favourite book"""
    print(f"The name of my favourite book is, {name_of_book.title()}!")

Book_title('Alice in womderland')

#funtion defination can have multiple parameters 
#Positional Arguement can be called by their position in the function defination
#keyword argument are arguments that can be called by their name.

#positional parsing & Keyword
def descirbe_pet(animal_type, pet_name, owner='Destiny'):
    """display information about pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}, has an owner {owner}")

descirbe_pet(pet_name='Desto', animal_type='Dami')
descirbe_pet('Dog', 'werey')
descirbe_pet('goat', 'isaac')
descirbe_pet('cow', 'blackson')

#task

#task for shirts with different sizes and finally with 
def make_shirt(size='Large', message='I love python'):
    """Print size and message of shirt"""
    print(f"The shoe size {size} and shows the message {message}")

make_shirt()
make_shirt('Medium')
make_shirt('L', 'I really love za Pton')
    
#task for display of cities with default country and finally with a different law
def describe_city(city, country='United States'):
    """Prints the name of a city and it's country"""
    print(f"{city.title()} is in {country.title()}.")

describe_city('New York')
describe_city('chicago')
describe_city('london', 'united kingdom')


#return value 
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a fullName neatly formatted"""
    full_name = f"\n{first_name} {middle_name} {last_name} "
    return full_name.title()

musician = get_formatted_name('jimi', 'jay')
musician = get_formatted_name('Happy', 'People')
print(musician)

#function into a dictionary 

def build_person(firstname, lastname, age=None):
    """Return a dictionary of infomation about a person"""
    person = {'first': firstname, 'last': lastname}
    if age:
        person['age'] = age
    return person

musical = build_person('jimi', 'saira', age=35)
print(musical)

def get_formattted_name(first_namee, last_namee):
    """Return a full name formatted"""
    fullnamee = f"{first_namee} {last_namee}"
    return fullnamee.title()
    
while True:
    print(f"\nPleasetell me your name")
    print("(Enter 'q' to quit execution)")
    f_name = input("First Name: ")
    if f_name == 'q':
        break
    l_name = input("Last Name: ")
    if l_name == 'q':
        break

    formattted_name = get_formattted_name(f_name, l_name)
    print(f"\nHello, {formattted_name}")

def city_country(city_name, city_count):
    """Return the name of the city and country it is in"""
    city = f"{city_name}, {city_count}"
    return f"\n{city_name.title()} {city_count.title()}"

print(city_country("'New York'", "'United States'"))
print(city_country("'New Jersy'", "'america'"))
print(city_country("'Land", "'Destiny Obs'"))
        
    
def make_album(artist, title, songs=None):
    """Builds Dictionary Describing a music"""
    album = {'artist': artist, 'title': title, 'songs': songs}
    return album

while True:
    print("\nEnter album information")
    print("(Enter 'q' to terminate)")

    artist = input("Artisit Name: ")
    if artist == 'q':
        break
    title = input("Title Name: ")
    if title == 'q':
        break

    song = input("Song Number (Optional): ")
    if song == 'q':
        break

    album = make_album(artist, title, song)
    print(album)

    
##passing a list

#write program that greet number of users

# def greet_people(names):
#     """Greeting users by names given"""
#     for name in names:
#         msg = f"Hello, {name.title()}"
#         print(msg)
#         return msg

# while True:
#     print("\nWhat is your name")
#     print("(Enter 'q' to terminate)")
#     name = input("Name: ")
#     if song == 'q':
#         break

# Username = f"Hello, {name.title()}"
# greet_people(Username)


def greet_people(names):
    """Greeting users by names given"""
    for name in names:
        msg = f"\nHello, {name.title()}"
        print(msg)
        

Username = ['hannah', 'tobi', 'justin']
greet_people(Username)



#adding data to a list of emmpy dictionaries using pop
#structuring code a little bit nicer

def print_models(unprinted_designs, completed_designs):
    """Simulate pricing each design, until none are left."""
    while unprinted_designs:
        current_designs = unprinted_designs.pop()
        print(f"Printing Model: {current_designs}")
        completed_designs.append(current_designs)

def show_completed_models(completed_designs):
    """Show all completed models"""
    print("\nThe following Designs are complete: ")
    for completed_design in completed_designs:
        print(completed_design)

unprinted_designs = ['Phone Case', 'Robot pendant', 'dodecaheron']
completed_designs = []

#creating slice from list
print_models(unprinted_designs, completed_designs)
#show_completed_models(completed_designs)

print(unprinted_designs)
print(completed_designs)
print("\n")

# make a short list of text and pass text in them
def Short_text(msgs):
    """Greeting users"""
    for msg in msgs:
        print(msg)
        

msgs = ['Hi', 'How are you?', 'Hello, beautiful']
Short_text(msgs)
print("\n")


def send_msgs(text_msg, sent_txt_msgs):
    """Print msg to and add them to another gorup"""
    while text_msg:
        current_msg = text_msg.pop()
        print(f"Available Msg: {current_msg}")
        sent_txt_msgs.append(current_msg)

def show_sent_text(sent_txt_msgs):
    """Show all sent text"""
    print("\nThe following Text are sent: ")
    for sent_txt_msg in sent_txt_msgs:
        print(sent_txt_msg)

text_msg = ['Hi', 'How are you?', 'Hello, beautiful']
sent_txt_msgs = []

send_msgs(text_msg[:], sent_txt_msgs)
show_sent_text(sent_txt_msgs)

print("\t")
print(text_msg)
print(sent_txt_msgs)
print("\t")



#*passing a number of arguments creating empty tuple 
def make_pizza(size, *topping):
    """Print the list of all possible toppings"""
    print(f"\nMaking a {size} - Pizza with the following topping: ")
    for toppings in topping:
        print(f"- {toppings.title()}")

make_pizza(16, 'pepperoni')
make_pizza(21, 'maggi', 'salt', 'sugar', 'tomato')


#creates an empty dictionary  
def build_profile(first, last, middle=None, **user_info):
    """Build a dictionary containing everything we know about a user"""
    user_info['first_name'] = first.title()
    user_info['last_name'] = last.title()
    user_info['Middle'] = middle.title()
    return user_info

user_profile = build_profile('Obueh', 'Destiny', 'Onyekachi', 
                             location = 'Lagos', field= 'Programiing')
print(user_profile)
 

def sandwich_ing(*args):
    """print a summary of the sandwich ing being ordered"""
    print("\nThese are the sandwich ingredients")
    for arg in args:
        print(f"- {arg}")
        # if arg == :
        #     print(f"- is empty")

sandwich_ing('')
sandwich_ing('salad', 'curry', 'maggi')
sandwich_ing('moi-moi')


def abt_car(manufac, model, **car):
    """Build a dictionary containing everything about a car"""
    car['Car Manufacturer'] = manufac.title()
    car['Car Model'] = model.title()
    return car

car = abt_car('sabaru', 'outback', color = 'blue', tow_package= False)
print(car)
 

