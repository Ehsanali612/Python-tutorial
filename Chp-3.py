#Here this is a list 
#[0],[1],the index number . in python & other languages index start's from --->0
#|
#|
# friends=['Ahmed','Khadim','Ilyas' ]
# print("Hi"+friends[0].title())
# print("Hi"+friends[1].title())
# print("Hi"+friends[2].title())
#Task-2
# items=["bora", "Chen"]
# if "bora" in items:
#     print("yes bora is available")
# elif "Chen" in items:
#  print("Sorry bora is not available but chen")
# else:
#  print("Nothing is available")

#append=Add new value to a list
# name=['ehsan']
# name.append('Ahmed')
# print(name)

# bicycles=['Trek ', 'C  nnend', 'Redline','Specilized']
# message="My fIRST Bicycle was "+ bicycles[0].title()+"."
# print(message)

# items=['Mango','Banana','Orange ']
# print(items[0]+'\n'+items[1]+'\n'+items[2]+'\n')

#  items=['Ahmed ', 'M jan ']
# msg=input("Enter Your Question ? \n")
# if 'Ahmed'in msg:
#    print("hi Ahmed How are you ")
# else:
#    print("Sorry M.Jan is Not here ")

# Append Elements to the End if The list 
""" list=['Car','Bus ', 'Bike ']
print(list)
list[0]="Hehehe"
print(list) """
# Append Elements to the End if The list 
""" list=['Motu','Patlu','Amaze']
list.append('Great')
print(list) """
#Inserting Elements into a List
# You can add a new element at any position in your list by using the insert()
# method. You do this by specifying the index of the new element and the 
# value of the new item.
""" list=[1,2,4,4,6,8,8]
list.insert(3,5)
#there three show index number by which we have to replace with
# my Desire Number 
print(list) """

# tO dELETE ANY ITEM FROM LIST USE " del " at start of variable name like 
""" list=['Ahmed','Ehsan', 'Brother']
del list[0]
print(list) 

"""
# Removing an Item Using the pop() Method
# Sometimes you’ll want to use the value of an item after you remove it from a 
# list. For example, you might want to get the x and y position of an alien that 
# was just shot down, so you can draw an explosion at that position. In a web 
# application, you might want to remove a user from a list of active members 
# and then add that user to a list of inactive members.
# The pop() method removes the last item in a list, but it lets you work 
# with that item after removing it. The term pop comes from thinking of a 
# list as a stack of items and popping one item off the top of the stack. In 
# this analogy, the top of a stack corresponds to the end of a list.
""" list=["hi","Great"]
print(list)
ul=list.pop()
print(list)
print(ul)
"""
# there .title() will capitalize  the word 1st latter
""" list=["hi","Great"]
ul=list.pop()
print("hi "+ul.title()+"\b"+"to meet you " + ".")  """
# Removing Element by value by .remove() method
''' list=["Hi",'How  are you']
list.remove('Hi')
print(list) '''
# ALSO
''' list=['Car  ','bike  ','Plane']
tooExpensive="Plane"
print("\n"+tooExpensive.title()+"Is Expensive for me")'''
#Sort method
# in this method this  will  sort  alphabet according  to alphabaticalorder
#as
''' list=["zeem","Xram","army","English"]
list.sort()
print(list)
'''
# for reverse  use reverse=True in sort methode like this sort(reverse=True)
'''  list=["zeem","Xram","army","English"]
list.sort(reverse=True)
print(list) '''

#Sorting a List Temporarily with the sorted() Function
''' list=["zeem","Xram","army","English"]
list.sorted()
print(list)
'''

#Printing a List in Reverse Order
''' list=["zeem","Xram","army","English"]
list.reverse()
print(list)'''

#  Determine the  length of the list
'''list=["zeem","Xram","army","English"]
print(len(list))'''

# to acess last item but you dont know the lentght use  this
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[-1])


