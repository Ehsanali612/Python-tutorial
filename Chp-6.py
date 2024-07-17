# Dictionaries
# A simple dictionaries
'''dict={
    'name':'Ehsan',
    'class' : "Bsc",
    'Department' : "Software Engineering"
}'''
# there name ,class or department are keys that holds different values eg..for name,its value is Ehsan
'''print(dict['class'])
print(dict['Department'])'''

# we can also aces to this
'''myName={
    'name':'Ehsan',
    'Proficient' :  'Student'
}
name = myName['Proficient']
print('This  is our  new \t' + name)'''

#Adding key value pairs in dictionary 
# Bcz Dictionaries are Dynamic 
#like
'''dict={
    'name':'ahmed',
     'Department':'Bs software Engineering  '
     }
print(dict)
dict['location']='Dera Bugti'
dict['University']='Khawaja fareed university'
print(dict)'''
# we can do same like this by an empty dictionaries
# like
'''dict={'Company':'Tesla'}
print(dict)
dict['name']='ahmed'
print(dict)'''
#we can also modify  this 
# as you can see i change the value of company from tesal to Vapar
'''dict['Company']='Vapar'
print(dict)'''
# Removing Key-Value Pairs
# When you no longer need a piece of information that’s stored in a dictionary, you can use the del statement
# like
'''dict={'Company':'Tesla'}
del dict['Company']'''
# there del used to delete 
'''print(dict)'''
# Note : Be aware that the deleted key-value pair is removed permanently.

# Looping Through a Dictionary:
# We  also loop dictionary:
'''userInformation={
    'name':'Ehsan',
    'City':'Dera Bugti'

}
for key,value in userInformation.items():
   '''
    # there the 'key '--> is the key like --->name
    # and value is the value of ----> name 
# .items()----> it tells that the-- value and key -- both should be display to python that are in python.

''' print('\nkey\t'+key)
    print('\nvalue\t'+ value)'''

'''Notice again that the key-value pairs are not returned in the order in 
which they were stored, even when looping through a dictionary.'''


# Looping Through All the Keys in a Dictionary
# The keys() method is useful when you don’t need to work with all of the 
# values in a dictionary.

'''favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
for keys in favorite_languages.keys():
    print('The name of person who name languages ' + keys.title())'''
# keys : keys only point keys 
# items : point both keys and values 
'''Looping through the keys is actually the default behavior when looping 
through a dictionary, so this code would have exactly the same output if you 
wrote . . .'''


'''cars={
    'ahmed':'suzuki',
    'ehsan':'Mean'
}
friendsCar=['ahmed ','Zulfaqar']
for name in friendsCar:
    print('Hi' + name)'''


# You can also use the keys() method to find out if a particular person 
# was polled. This time, let’s find out if Erin took the poll:
'''favoriteLanguage={
    'eric':'python',
    'ahmed':'c++',
    'ehsan':'assembly'
}
if 'jan'  not in favoriteLanguage.keys():    
   print("Please enter you favorite language")
else:
   print('darka aaray')'''

# The keys() method isn’t just for looping: It actually returns a list of all 
# the keys, and the line at u simply checks if 'erin' is in this list. Because 
# she’s not, a message is printed inviting her to take the poll:


# Looping Through a Dictionary’s Keys in Order

# You can use the sorted() function to get a copy of 
# the keys in order:
'''favoriteLanguage={
    'eric':'python',
    'ahmed':'c++',
    'ehsan':'assembly'
}
for  name in sorted(favoriteLanguage.keys()):
    print(name.title()+' \b thanks  you for taking the poll')'''

# Looping Through All Values in a Dictionary
'''If you are primarily interested in the values that a dictionary contains, 
you can use the values() method to return a list of values without any keys.'''


'''favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
for languages in favorite_languages.values():
    print(languages+' This is favorite language of  many people ')'''


#set()
'''When you wrap set() around a list that contains duplicate items, Python 
identifies the unique items in the list and builds a set from those items.'''
'''favoriteCars={
    'ahmed':'Mercedes ',# type: ignore
     'Ehsan': 'Suzuki',
     'Coli':'Megan',
     'zulfaqar':'Megan'
     }
for  cars in set(favoriteCars.values()):
    print(cars.title())
'''
# Nesting
'''Sometimes you’ll want to store a set of dictionaries in a list or a list of 
items as a value in a dictionary. This is called nesting. You can nest a set 
of dictionaries inside a list, a list of items inside a dictionary, or even a 
dictionary inside another dictionary'''
#A list of Dictionaries :
'''The alien_0 dictionary contains a variety of information about one alien, 
but it has no room to store information about a second alien, much less a 
screen full of aliens.'''

# for eg

'''ahmed={'Hi':'to', 'you':'my','friend':'Thankyou'}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens=[ahmed,alien_1,alien_2]
for alien in aliens:
    print(alien)
'''


# Make an empty list for storing aliens.
'''aliens = []
# Make 30 green aliens.
for alien_number in range(30):
   new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
aliens.append(new_alien)'''
 
# Show the first 5 aliens:
'''for alien in aliens[:5]:
 print(alien)
print("...")
# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))
'''
# A List in a Dictionary
'''Rather than putting a dictionary inside a list, it’s sometimes useful to put 
a list inside a dictionary.'''
'''pizza={
  'crust':'thick',
   'toppings': ['mushrooms', 'extra cheese'],
}
print(f'You oder a {pizza["crust"]} -crust pizza')
for topping in pizza['toppings']:
  print('\t '+topping )'''



# A Dictionary in a Dictionary
'''You can nest a dictionary inside another dictionary, but your code can get 
complicated quickly when you do.'''


'''pizza={
    # this is nested dictionary inside a dictionary
    'pizar':{
        'pizza1':'Chicken pizza',
        'pizza2':'miken pizza'
    }
}

for name, users in pizza.items():
    print( pizza['pizar'])

'''
