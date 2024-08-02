# Handaling zero ZeroDivisionError Exception
# like this 
'''print(5/0)'''
# it showing ZeroDivisionError bcz we can't divide 5 by 0
# SO we will use try , except block
# like
'''try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero")
    '''
# If the code in try block occurs any  error the python will execute
# except block
#  You can also do this for file not found 
file_name = 'alice.txt '
try:
    with open(file_name) as file_object :
        contents = file_object.read()
except FileNotFoundError:
    msg = " Soryy the {} does not exsit " .format(file_name)
    print(msg)