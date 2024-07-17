# function
''' A function makes our work easy so don't have to write a lot of codes '''
# For eg
'''def greet_users():'''
# def ---> defines a function ,or its called function definition
# without def a function can't  execute.
# greet_users()---> its function name you can name it any thing 
# it curly brackets you can assign variables  or parameter like greet_users(name)
# after that ---> function body  comes in  which print('hello') is now
'''print('Hello')'''
'''at last a  function name  comes again which means we are calling function
    _>  and  we can assign a variable or parameter  value to it '''
# greet_users()

'''def greet(name,city):
    print(f'{name} lives in {city}')
greet('Ehsan Ali','Dera  Bugti')'''

'''People sometimes speak of arguments and parameters interchangeably. Don’t be surprised if you see the variables in a function definition referred to as arguments or the variables in a function call referred to as parameters.'''

# We can call multiple functions as we want 
# lIKE 
'''def greet(name):
    print(f'{name}')
greet('Ehsan')
greet('Ahmed')'''

# Order Matters in Positional Arguments

'''def describe_pet(animal_type, pet_name):'''
 
"""Display information about a pet."""
 
''' print("\nI have a " + animal_type + ".")
 print("My " + animal_type + "'s name is " + pet_name.title() + ".")
 
describe_pet('harry', 'hamster')'''


'''In this function call we list the name first and the type of animal second. 
Because the argument 'harry' is listed first this time, that value is stored in 
the parameter animal_type. Likewise, 'hamster' is stored in pet_name. Now we 
have a “harry” named “Hamster”:'''

# Keyword arguments
# we can use keyword  arguments like
'''def greet(name):
    print(f'{name}')
greet(name='Ehsan')'''
# make  sure wee use it perfectly

# Default values
'''def describe_pet(pet_name, animal_type='dog'):
 """Display information about a pet."""
 print("\nI have a " + animal_type + ".")
 print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='willie')'''

# return function
'''def greetings(name,city,address):
 full_address= name+'\b' + city + '\b' + address
 return full_address.title()
man=greetings('Ehsan ',' Dera Bugti ', 'Zin Koh ')
print(man)
'''
# Returning a dictionary

'''def buildPerson(firstName,LastName):
 person={'first':firstName,'Last':LastName}
 return person
musician=buildPerson('Ehsan','Ali')
print(musician)
'''
# as you can practice this 
'''def buildPersons(firstName , lastName , middle_name=''):
 person={'first': firstName , 'Last':lastName}
 if  middle_name:
    person['middle_name']=middle_name
 return person

musician = buildPersons('Ehsan','Bugti', middle_name='Ali')
print(musician)'''


# Using a function with a while loop 

'''def  name(firstName , lastName):
    fullname =firstName + " " + lastName
    return fullname
while True:
    first=input("Enter you first name :")
    last=input('Enter your last : ')
    names=name(first,last)
    # Make sure to not use ---> names=name(first+last)
    # bcz it acts as single argument 
    print("hello "+ names)'''
#2

'''def  get_formatted_name(firstName,lastName):
    fullName = firstName + lastName
    return fullName
while True:
    print("\n Tell  me your name : ")
    print("(Enter 'q' to quite the program )")

    f_name=input("Enter first name : ")
    if f_name == 'q':
        break
    l_name=input(" Enter  last name ")
    if l_name == 'q':
        break
    formattedName=get_formatted_name(f_name,l_name)
    print(" Hello " + formattedName + " ! ")'''

#Modifying a List in a Function
'''When you pass a list to a function, the function can modify the list. Any 
changes made to the list inside the function’s body are permanent, allowing 
you to work efficiently even when you’re dealing with large amounts of data.'''

# start with design that need to be printed

'''unprinted_design=['IphoneCAse','robotPendent ','dodecagon']
printed_design=[]
while unprinted_design:
  current_design=unprinted_design.pop()
  print('Printing Model : '+ current_design)
  printed_design.append(current_design)
print("The Following has been printed")
for completeModels in printed_design:
  print(completeModels)'''

  # THERE FIRST IT WILL PRINT DODECAGON BCZ 
"""
  ___________
  |         |
  |iphoneCase|
  |_________|
  |robotPendent|   ------>   There  when we append a value from one list to 
  |DODECAGON|                 an another empty list ,then it reveres ,like in 
   _________                 the place of iphoneCase there will be dodecagon,
                              etc..So on.
  """
# to make it organize of more efficient
# we can put it into a function

'''def  printed_models(unprinted_design,printed_design):
    while unprinted_design :
        current_design=unprinted_design.pop()
        print('Printed Design : ' + current_design)
        printed_design.append(current_design)
def Complete_models(printed_design):
    print("The following models have  been printed : ")
    for complete_model in printed_design:
     print(complete_model)

unprinted_design=['iphone case', 'robot pendant', 'dodecahedron']
printed_design=[]'''

# Now we will call the functions
# we should create separate
'''printed_models(unprinted_design[:],printed_design)'''
# Rather than emptying first list , WE COPY [:] the unprinted_design
'''
                                             |
                                             |
                                             |
                                             |
                                             This is  slice notation make  copy of the the list to send the function 

                                             1) -> But this time it only print 
                                             copy of  the unprinted_design:
'''
'''Complete_models(printed_design)'''
#  these both above codes will have same output

# PASSING AN ARBITRARY  NUMBER OF ARGUMENTS:
'''
The function in following parameter *Toppings but collects as many arguments as 
the calling provides .
for e.g.
'''
'''def pizza(*Toppings):
    # the an asterisk (*) in _____>  pizza(*Toppings) 
    for pizzas in Toppings:
        print('-'+pizzas)'''
'''                                  |
                                           |
                                           |
                                           _
                                           -
                                           say that make an empty tuple
                                           called Toppings.
                                            
   Print the list of topping that have been requested'''
'''
pizza('Pepperoni')
pizza('Mushroom','Green Pepper ', 'Extra Cheese')
'''
# Mixing positional and arbitrary arguments
'''
def pizza(size , *toppings ) :
    print('\n Making a' + str(size)+ '- inch pizza  with the following toppings')
    for topping in toppings:
        print("-"+topping)
pizza( 19 ,'Pepperoni')
pizza( 20 ,'Mushroom','Green Pepper ', 'Extra Cheese')
'''
# Using arbitrary keywords arguments

# def build_profile(first,last,**user_info):
'''
     The 
double asterisks before the parameter **user_info cause Python to create 
an empty dictionary called user_info and pack whatever name-value pairs it 
receives into this dictionary
    '''
'''profile={} 
    profile['first_name']='first' 
    profile['last_name']='Last'
    for key , value in user_info.items():
        profile[key]=value
    return profile
 
user_profile=build_profile(
    'albert einstein ', 'Newton ',
    location='princeton',
    field='Physics'
)    
print(user_profile)'''

# Storing our function in modules
'''An import statement tells Python to 
make the code in a module available in the currently running program file.
'''
# Importing an  Entire Module 
''' A module is a file ending in .py that contains the code you want to import into your Functions program
'''
# we create a python file name *pizza.py*  and then import it here 
'''import pizza
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')'''
# Importing  Specific function:
# You can also import a specific function from a module.

# from  pizza import make_pizza 

'''In this we saying that from module or file pizza.py  __>import 
specific  function name make_pizza'''
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using ' as ' to  give  function an Alice
# for eg  imported  function is too long  so for that we will  use __>as
# for eg ---> pizza--->as >>> pz
'''from  pizza import make_pizza as  pz'''
# you can  give alias to modules like this  
# import pizza as pz

'''pz(16, 'pepperoni')
pz(12, 'mushrooms', 'green peppers', 'extra cheese')
'''
# To import all function from  a module use * like this
'''from pizza import *'''
# and so on
'''make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')'''
