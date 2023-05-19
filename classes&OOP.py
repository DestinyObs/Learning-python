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

    def __init__(self, restaurant_name, cuisine_type,):
        self.restuarant_name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = numbers_served = 0
    
    #another method
    def describe_restaurant(self):
        """Describing a resturant"""
        print(f"The restuarant is called {self.restuarant_name}.")
        print(f"the cuisine type is {self.cuisine}.")

    def open_restuarant(self):
        """Saying the restaurant is now opened"""
        print(f"{self.restuarant_name} is now opened")

    def set_number_served(self, guest):
        """Set the number of sevred customers to a given value"""
        self.number_served = guest
    
    def increament_number_Served(self, increament):
        """Increamenting the number served in the the process"""
        self.number_served += increament
    

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

restaurant = restaurant('Destiny', 'Dami')
print(f"Number of Served Customers: {restaurant.number_served}")
print("-----")

restaurant.number_served = 200
print(f"Number of Served Customers: {restaurant.number_served}")
print("----")

restaurant.set_number_served(400)
print(f"Number of Served Customers: {restaurant.number_served} \n")
print("----")

restaurant.increament_number_Served(500)
print(f"Number of Served Customers: {restaurant.number_served} \n")
print("----")


class User:
    """"simple class for a user"""
    def __init__(self, first_name, last_name, location=None, age=None):
        self.firstname = first_name
        self.lastname = last_name
        self.location = location
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        """Describing the user"""
        print(f"This user's names are {self.firstname.title()} {self.lastname.title()}.")
        print(f"This user is located at {self.location} and is {self.age} years old")

    
    def greet_user(self):
        """Greeting a user"""
        print(f"Hello {self.lastname} {self.firstname}. \nHow are you doing today? ")

    def increament_login_attempts(self):
        """increamenting the login attempts"""
        self.login_attempts += 1

    def rest_login_attempts(self):
        """Reset Number of login attmepts to 0"""
        self.login_attempts = 0



user_1 = User('destiny', 'Obueh', 'Lagos', 19)

user_1.describe_user()
user_1.greet_user()
print("---")
user_1.increament_login_attempts()
user_1.increament_login_attempts()
user_1.increament_login_attempts()
print(f"Login attempts: {user_1.login_attempts}")
print("----")

user_1.rest_login_attempts()
print(f"Login attempts (after rest): {user_1.login_attempts}")
print("\n")



class car:
    """a simple attempt to represent a car"""

    def __init__(self, model, make, year, color):
        """initailizing attributes to describe a car"""
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.odometer_reading = 0 

    def get_desciprive_name(self):
        """Return a neatly formatted desciptive name"""
        long_name = f"{self.make} {self.model} {self.color} {self.year}"
        return long_name.title()
    def read_odometer(self):
        """print a statement showing the car's in mileage"""
        print(f"This car has {self.odometer_reading} miles one it")
    
    def update_odo(self, mileage):
        """
        Set the odo value to a given value 
        reject the change if it tries to roll the odo back
        """
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an ODO")
    def increament_odometer(self, miles):
        """add the given amuont to the previous amount"""
        self.odometer_reading += miles


my_new_car = car('BMW', '4-matic', 2023, 'blue')
print(my_new_car.get_desciprive_name())
# odo = input("Odometer Reading: ")
my_new_car.odometer_reading = 345
my_new_car.read_odometer()

my_new_car.update_odo(341_600)
my_new_car.read_odometer()

my_new_car.increament_odometer(100 )
my_new_car.read_odometer()
print("---")

class ElecreicCar(car):
    """"
    Initialize attribute of the parent class
    then initailize attributes specific toan electric car
    """
    def __init__(self, model, make, year, color):
        """initializing attribtes in parents"""
        super().__init__(model, make, year, color)

my_tesla = ElecreicCar('Model S', 'Telsa', '2022', 'grey')
print(my_tesla.get_desciprive_name())
