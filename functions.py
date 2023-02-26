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