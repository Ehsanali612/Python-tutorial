# Loops 
# for loop
''' magicians=['David ','Bk Brand ','Robin']
for magician in magicians: '''
#This line tells Python to retrieve the first value from the list magicians
'''and store it in the variable magician.
    print(magician)'''
#pactice
''' boys=['ahmed  ', 'ehsan ', 'm.jan']
for  boy in boys:
    print(boy.title()+ "Are  great boys ")
    print("I can't wait to see your next trick,"+boy.title()+'.\n')
    #Doing Something After a for Loop
    #Thank  You to these guys
    print("Thank  You ! guys for your honour able speech")'''
#practice Task #1)
''' pizza=['Chicago Style',
'Brick Oven',
'Italian ',
'Neapolitan ']
print('how much you like .')
for  pizzas in pizza:
    print('I like  '+ pizzas.title()+
'pizza')
print("I really love pizza!")
    '''
#practice Task #2)
'''pets=['dog','cat','goat']
for pet in pets:
    print('A '+pet.title() +' would make a great pet.')'''
 
# Using Range Function
'''for value in range (1,5):
    print(value)'''
# this will print values from 1 to 5 

#Using range() to Make a List of Numbers
'''number=list(range(1,6))
print(number)'''
#also
'''for i in range(2,20,4):
    print(i)'''
# there it start from 2 to 18 with gap of 4 

'''squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)
print(squares)'''
# for more clean code
'''squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)'''
# you can also use it as
'''sqaure=[value**2 for value in range(1,11)]
print(sqaure)'''
# Simple Statistics with a List of Numbers
'''digits=[1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))'''

# Slicing a List
'''players=['Robin ','Micheal ','Ronald','Jesus','Moses']
print(players[0:3])'''
# it will print 1st three players Robin to  Ronald 
'''You can generate any subset of a list. For example, if you want the second,
 third, and fourth items in a list, you would start the slice at index 1 and 
end at index 4'''
'''players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])'''
# This time the slice starts with 'martina' and ends with 'florence':

# If you omit the first index in a slice, Python automatically starts your 
# slice at the beginning of the list:
'''players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])'''
#another
'''players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])'''
# There this code will index last 2(0,to 2)
#like from michael (there this is zero) to eli (where this is eli)
'''players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])'''
# This prints the names of the last three players and would continue to 
# work as the list of players changes in size.


# loop through slice 

'''slice=['Ahmed','Ehsan','M.jan']
print('Here is the first Two   players in my team ')
for slices in slice[:2]:
    print(slices.title())
'''

#Copying a List
# To copy a list, you can make a slice that includes the entire original list 
# by omitting the first index and the second index ([:]). This tells Python to 
# make a slice that starts at the first item and ends with the last item, producing a copy of the entire list.
'''my_foods=['pizza','Falefel','Carrot  Cake']
frinds_food=my_foods[:]
my_foods.append('BBQ')
frinds_food.insert(0,'Ice cream')
print("My favorite food is.")
print(my_foods)
print("\n My friends  favorite food is .")
print(frinds_food)'''

# instead of  this  we can also write like this
'''my_foods = ['pizza', 'falafel', 'carrot cake']
# This doesn't work:
friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)'''

'''Tuples
Lists work well for storing sets of items that can change throughout the 
life of a program. The ability to modify lists is particularly important when 
you’re working with a list of users on a website or a list of characters in a 
game. However, sometimes you’ll want to create a list of items that cannot 
change. Tuples allow you to do just that. Python refers to values that cannot 
change as immutable, and an immutable list is called a tuple.'''

'''Defining a Tuple
A tuple looks just like a list except you use parentheses instead of square 
brackets. Once you define a tuple, you can access individual elements by 
using each item’s index, just as you would for a list.'''

'''tupLe=('Ehsan','Ahmed','Dostan')
print(tupLe[0])
print(tupLe[2])'''
#but what happen if we try to change the inside value of tuple 
#let me see
'''tuple[0]='Great'''
# you can see it will through Error bcz tuple  can't be changed

# looping  through Tuple
'''Dimensions=(200,0)
for Dimesion in Dimensions:
    print(Dimesion)'''

# Writing over a Tuple
# Although you can’t modify a tuple, you can assign a new value to a variable 
# that holds a tuple. So if we wanted to change our dimensions, we could 
# redefine the entire tuple:


'''Dimensions=(200,0)
print("Original dimensions:")
for Dimesion in Dimensions:
    print(Dimesion)'''
# Here we can't modify tuple
#But
# we can re-define  our tuple
'''Dimensions=(500,200)
print('\n Modified Dimensions')
for Dimension  in Dimensions:
    print(Dimension)'''

#Coding Style
# for better coding
# indentation
''' PEP 8 recommends that you use four spaces per indentation level.
 Using four spaces improves readability while leaving room for multiple levels of 
indentation on each line'''
# Line Length
'''Many Python programmers recommend that each line should be less than 
80 characters.

PEP 8 also recommends that you limit 
all of your comments to 72 characters per line, because some of the tools 
that generate automatic documentation for larger projects add formatting 
characters at the beginning of each commented line.'''

# Blank Lines
'''To group parts of your program visually, use blank lines. You should use 
blank lines to organize your files, but don’t do so excessively. By following 
the examples provided in this book, you should strike the right balance. For 
example, if you have five lines of code that build a list, and then another 
three lines that do something with that list, it’s appropriate to place a blank 
line between the two sections. However, you should not place three or four 
blank lines between the two sections.
Blank lines won’t affect how your code runs, but they will affect the 
readability of your code. The Python interpreter uses horizontal indentation to interpret 
the meaning of your code, but it disregards vertical 
spacing'''

