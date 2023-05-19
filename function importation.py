import functions
#import functions
#use from module_name import function_name



functions.make_pizza(16, 'pepperoni')
functions.make_pizza(21, 'maggi', 'salt', 'sugar', 'potatoe')


#importing a function from our entire module
from functions import sandwich_ing
sandwich_ing('buns', 'maggi', 'curry')
sandwich_ing('akara')

#we could also use an alias 

#from functions import * but it is not advised 
#every function to 


import functions
unprinted_designs = ['Phone Case', 'Robot pendant', 'dodecaheron']
completed_designs = []
functions.print_models(unprinted_designs, completed_designs)
functions.show_completed_models(completed_designs)


from functions import make_pizza as MP
MP(16, 'pepperoni')

import functions as F
F.make_pizza(12, 'maggi')


from functions import *
make_pizza(12, 'salt')

courses = "nnew one"
print(courses)


#OOP oriented programming 

