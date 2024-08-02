'''Refactoring
Often, you’ll come to a point where your code will work, but you’ll recognize that you could improve the code by breaking it up into a series of functions that have specific jobs. This process is called refactoring. Refactoring 
makes your code cleaner, easier to understand, and easier to extend. 
We can refactor remember_me.py by moving the bulk of its logic into one 
or more functions. The focus of remember_me.py is on greeting the user, so 
let’s move all of our existing code into a function called greet_user()'''
import json
def get_stored_username():
    '''Get Stored username if available .'''
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
def greet_user():
    'Greet hte user by name '
    username = get_stored_username()
    if username:
        print("Welcome back ," + username + '!')
#  This function retrieves a stored username and returns 
# the username if it finds one. If the file username.json doesn’t exist, the function returns None
    else:
        username = input('What is ur name :')
        filename = 'username.json'
        with open(filename,'w') as f_obj:
            json.dump(username,f_obj)
            print("We ll remember you when you come back ," + username + "!")
greet_user()