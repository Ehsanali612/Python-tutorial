# message=input("\b Please  enter your name : ")
# print("Hi "+ message + "\b how are u ")
#2

'''prompt='If you tell us how are , so we can personalized a message for you'
prompt +="\n What's Your first name :"
name =input(prompt)
print("\nHello, " + name + "!")

'''
'''This example shows one way to build a multi-line string. The first line 
stores the first part of the message in the variable prompt. In the second line, 
the operator += takes the string that was stored in prompt and adds the new 
string onto the end'''

#3
# Using int to accept numerical input

'''age = input("Enter Your age : ")
age = int(age)'''

'''We can resolve this issue by using the int() function, which tells 
Python to treat the input as a numerical value. The int() function converts a string representation of a number to a numerical representation,'''

'''if age >= 18:
  print(True)
else:
  print(False)'''

# The Modulo Operator
'''A useful tool for working with numerical information is the modulo operator (%), which divides one number by another number and returns the remainder:'''

'''num=3%2
print(num)'''

# This will return reminder of a number:

# Even or odd the in python :

'''num=input("Enter your number ")
num=int(num)

if num%2==0:
    print(f'The num {num} is Even  ')
else:
    print('This is odd')'''
# If you are using python 2.7 use raw_input() than input()



# Introducing while Loops
'''The for loop takes a collection of items and executes a block of code once 
for each item in the collection. In contrast, the while loop runs as long as, 
or while, a certain condition is true.'''

# current_number=10
# while current_number<=20:
#     print(current_number)
#     current_number+=1


# Letting the User Choose When to Quit

'''prompt='Tell  me something that i will  repeat back : '
prompt+='\n Enter Quite to end the program '
message=""
while message != 'Quite':
    message=input(prompt)
    print(message)
    '''
    # Using a Flag
    
#  define one variable that determines whether or not the entire program is active. This variable, called a flag, acts as a signal to the program.

'''prompt= 'Tell something that i will repeat'
prompt+='Enter a program to  Quite the program '
active=True
while active:
    message=input(prompt)
    if message=='quite':
        active==False
    else:
        print(message)'''
# Using break to Exit a Loop
'''To exit a while loop immediately without running any remaining code in the 
loop, regardless of the results of any conditional test, use the break statement.'''

'''prompt='\ntell me something that i will repeat '
prompt+='\nEnter progname to quite '
while True:
    city=input(prompt)

    if city =='Quite':
        break
    else:
        print(f'I would love to go {city.title()} !')
'''

# A loop with while true continue forever even when an break statement used 
# Using continue in a Loop
'''Rather than breaking out of a loop entirely without executing the rest of its code, you can use the continue statement to return to the beginning of the 
loop based on the result of a conditional test.'''

'''current_num  = 0
while current_num <= 10:
    current_num  +=1
    if current_num %2 == 0:

#  The if statement then checks the modulo of current_number and 2.

        continue
    print(current_num)'''

'''   If the modulo is 0 (which means current_number is 
divisible by 2), the continue statement tells Python to ignore the rest of 
the loop and return to the beginning.
'''
# Avoiding Infinite Loops
'''Every while loop needs a way to stop running so it won’t continue to run forever. For example, this counting loop should count from 1 to 5:'''

'''num=0
while  num <= 5:
    print(num)
    num +=1'''
    # This will run till req meet 5
    # but
    
# num=0
# while num <=6:
#         print(num)

# Moving Items from One List to Another
'''Consider a list of newly registered but unverified users of a website. After 
we verify these users, how can we move them to a separate list of confirmed 
users?'''

'''conformUsers = ['Ahmed','Zulfaqar','Ehsan']
Not_Conform=[]
while Not_Conform:
    currentUser=conformUsers.pop()
    print(" Verifying :" + currentUser.title())
    Not_Conform.append(currentUser)

print("\n The following users has been conformed ")
for conformUser in conformUsers: 
    print(conformUser.title())
    '''

# Removing All Instances of Specific Values from a List
'''In Chapter 3 we used remove() to remove a specific value from a list. The 
remove() function worked because the value we were interested in appeared 
only once in the list'''

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
 pets.remove('cat')
 
print(pets)


# Filling a Dictionary with User Input

'''You can prompt for as much input as you need in each pass through a while
loop. Let’s make a polling program in which each pass through the loop 
prompts for the participant’s name and response. We’ll store the data we 
gather in a dictionary, because we want to connect each response with a 
particular user:'''

