cars=['audi','bmw','suzuki','helicopter']
for  car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())
# here first it will check that is there car name 'bmw' or not
#if there is car name bmw in then it will uppercase the bmw only
# else there any other car it will title() case them mean first letter remain capital else others 

car='BMW'
# this is simply used when we simply Assign a value to our variable
car=='BMW'
#it check whether its true or false ,by different conditions
''' if there car==BMW it will through true answer 
    But if  car= bMw it will trough false 
    bcz its strict equality operator so it have to be this mandatory'''

'''If case matters, this behavior is advantageous. But if case doesn’t matter 
and instead you just want to test the value of a variable, you can convert the 
variable’s value to lowercase before doing the comparison:'''
#like
car='bmw'
car.upper()=='BMW'
print(car.upper()=='BMW')
#it will print true bcz there the lower case bmw converted to uppercase so it becomes true  .
#and if the assigned value in upper so do do this as lower case as well.
# like 
car.lower()=="BMW"
'''If its lower it will threw 'true' but if upper case it will threw false'''
#another is  Not Equal to operator
# like
name='ehsan'
if name!='ehsaan':
    print(True)
    #there it will print true bcz ,name is not equal to ehsan its ehsaan.
    #But if it was ehsan it will not print bcz these were equal now.
else:
    print("Hi ! How are You")
# there are also some other
'''
>>> age = 19
>>> age < 21
True
#there it will threw true bcz 19 is less than 19
>>> age <= 21
True
cccc
>>> age > 21
False
#there it will threw False bcz 21 is greeter than 19
>>> age >= 21
False
#  there it will threw False bcz age is greater  then or Equal to 21

'''
# Using 'and 'to Check Multiple Conditions
name='ehsan'
nameTwo='Ahmed'
if name=='ehsan' and nameTwo=='Ahmed':
     '''It will pint true if both   if each test passes, the overall expression evaluates to True. If either test fails or if both tests fail, the 
expression evaluates to False.'''
     print(True)
else:
     # Else it will print False
    print(False)

num1=11
num2=12
num1 >= 12 or num1<=12
print(True)
# In the 'or ' condition if either one side is true it will print true for eg, there there right of or is true thats  why it returns true . same like for below statement.
# If both are false it will print false
num2 >=12 or num2 <=12
print(True)

name=['ahmed','ehsan','ijaz','ehsan']
if "ahmed" in name:
    print("Great you are already in list")
    # There it will print this if the ahmed is in list else it will print nikal bhosre ka 
else:
    print('Nikal bhosre ka')

# Other 
banned_Users=['ahmed','ehsan','martin']
name='ahmed'
if name in banned_Users:
    print(f'Sorry {name.title()} this user is in banned list')
else:
    print('')

# Bolean 
# Boleaan may be either 'True' or '  false'
# e.g
# name=True
# name=False

# conditional statements ,if ,elif ,else
#Advance 
size=18
if size<10:
    price=10
elif size<=18:
    price=20
    # we can add many elif statements as we want:
else:
    price=40
print(f'Your window cost is $ { str(price)} .')
'''Else is not mandatory if your work is done with elif then its ok to ommit else.'''
name=['ehsan','ahmed','shams','jan']
for names in name:
    print(f'{names.title()} are present in the class')

# Checking That a List Is Not Empty
requested_pizza=[]
if requested_pizza:
    for pizas in requested_pizza:
        print("Adding " + requested_pizza + ".")

# first it checks if the there any value in the requsted it will print the if ---> statements , else if the list is empty it will print else statement:
'''else:
    print(f'Pizza is on the way ! Do you really need a good pizza')'''

# Using multiple list 
available_toppings = ['mushrooms', 'olives', 'green peppers',
 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requesetedToppings in requested_toppings:
    if requested_toppings in available_toppings:
        print("Adding " + requesetedToppings+ ".")
else:
        print("Sorry, we don't have " + requesetedToppings+ ".")
print("\nFinished making your pizza!")
