# Counting to Twenty
'''for i in range(0,21):
    print(i)'''
# One  to one  Million in range :
'''number=list(range(1,100000))
print(number)'''

'''. Summing a Million: Make a list of the numbers from one to one million, 
and then use min() and max() to make sure your list actually starts at one and 
ends at one million. Also, use the sum() function to see how quickly Python can 
add a million numbers.'''
# number=list(range(1,100000))
# print(sum(number))
# print(max(number))
# print(sum(number))

'''. Odd Numbers: Use the third argument of the range() function to make a list 
of the odd numbers from 1 to 20. Use a for loop to print each number.'''
# for value in range(1,20,2):
#     print(value)
'''Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to 
print the numbers in your list'''
# number=[value*3 for value in range(3,30)]
# print(number)
'''Cubes: A number raised to the third power is called a cube. For example, 
the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that 
is, the cube of each integer from 1 through 10), and use a for loop to print out 
the value of each cube.'''
'''list=[]
for list in range (1,10):
     print(list**2)'''
# You  can also use like this 
'''number=[list**2 for list in range (1,10)]
print(number)'''

# Another
#  Use a list comprehension to generate a list of the 
# first 10 cubes.
'''digits=[(list(value**2 for value in range(1,10)))]
for digit in digits:
    print(digit)'''

#Slices
'''user=['Ahmed','Ehsan','ND','Qurban','Ahmer','Awais','Mk ','Jk','zk']
print(' The first three items in the list are')
print(user[0:3])'''
#there 0, is  starting point like Ahmed
# and 3 is end point like ND 
'''print(' Three items from the middle of the list are:')
print(user[3:6])'''
#The last three items in the list are:
'''print('The last three items in the list are:')
print(user[-3:])'''
#there if you only write 3 this will print from Qurban 
# So you have to write -3 for last 3 iNDEXES

# here its tuple -----> Basically tuples can't change 
resturentMenu=('Pizza','Orange','Mangp-shake')
for resuturent in resturentMenu:
    print(resuturent.title()+"are delicious foods")
# resturentMenu[2]='Great'
'''This will through an eRROR !'''
# Modified 
resturentMenu=('Pizza','Biscuit','Bracket')
for resuturent in resturentMenu:
    print(resuturent.title()+"are delicious foods")

    