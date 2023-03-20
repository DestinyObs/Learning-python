# Classes
# they have objectes of a class
# instnace of a calss is called an Object


class Dog:
    """A simple model of a dog"""
    def __init__(self, name, age, size=None): #called automatically anytime an object is created 
        """initialize name and age attributes"""
        self.name = name
        self.age = age
        self.size = size
    
    def sit(self):
        """Simulate a dog sitting in reponse to a command"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """stimulation is rolling over to a command"""
        print(f"{self.name} rolled over ")

my_dog = Dog('dami', 9, 10)
your_dog = Dog('winnie', 5, 1)

#dot notation
print(f"my dog's name is {my_dog.name.title()}")
print(f"my dog's age is {my_dog.age} Years Old")
print(f"my dog's size is {my_dog.size}kg")
print("\n")
my_dog.sit()
my_dog.roll_over()


print(f"Your dog's name is {your_dog.name.title()}")
print(f"your dog's age is {your_dog.age}")
print(f"your dog's size is {your_dog.size}kg")
your_dog.sit()
my_dog.roll_over()
print("\n")

class restaurant:
    """simple restaurant class"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restuarant_name = restaurant_name
        self.cuisine = cuisine_type
    
    #another method
    def describe_restaurant(self):
        """Describing a resturant"""
        print(f"The restuarant is called {self.restuarant_name}.")
        print(f"the cuisine type is {self.cuisine}.")

    def open_restuarant(self):
        """Saying the restaurant is now opened"""
        print(f"{self.restuarant_name} is now opened")

french_rest = restaurant('Destiny Obs', 'French')
japa_rest = restaurant('luigi', 'italian')
korean_rest = restaurant('curry', 'maggi')
naija = restaurant('Dami', 'obs')

french_rest.describe_restaurant()
print("---")
japa_rest.describe_restaurant()
print("---")
naija.describe_restaurant()
print("---")
korean_rest.describe_restaurant()
print("---")


class User:
    """"simple class for a user"""
    def __init__(self, first_name, last_name):
        self.firstname = first_name
        self.lastname = last_name

    def describe_user(self):
        """Describing the user"""
        print(f"This user's details are {self.firstname,} {self.lastname}.")
    
    def greet_user(self):
        """Greeting a user"""
        print(f"hello {self.lastname}, How's the {self.firstname} family. \t i hope you are all good?")


user = User('mary', 'jane')
user = User('mary', 'jane')
user = User('mary', 'jane')




    