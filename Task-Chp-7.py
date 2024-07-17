# Rental Car
'''user=input("What kind of rental car you would like : \n")
car=['suzuki']
for cars in car:
    print("Yes "+ cars +"  Is available ")'''

#  multipleOften

'''num=int(input("Enter the number "))
if num%10==0:
    print("This  number is multiple of zero ")
else:
    print('Sorry you are not a women ')
#3
# pizza toppings
prompt = " \n Enter a series of pizza toppings"
prompt += "\n Enter Quite to end program "
while True:
    pizza=input(prompt)

    if pizza=='Quite':
       break

    else:
       
       print(f'Your {pizza} pizza will be created soon ')
'''
# Movie ticket Price generator

'''Avg_age=12
while True :
    Movie_ticket=int(input(' Please Enter your age to get ticket price : \n'))
    if Movie_ticket<=3:
        print('\n Congratulations ! Your ticket is free ')
    elif Movie_ticket==3 or  Movie_ticket <=12:
        print(" \n Your Movie Ticket is $10 ")
    else:
        print("\n The Movie Ticket is $15 for You people")'''

response={}
#  set the flag indicates that polling is active 
polling_active=True
while polling_active:
    name=input('\n Enter you have Name ')
    response=input("Which mountain would you like to climb someday? ")
    response[name] = response
    
    repeat=input("Would you like to respond (yes/ no)")
    if repeat=='no':
        polling_active=False
print('______Poll-Result______')
for  name , responses in response.items():
    print(f"{name} would like to climb {responses}.")
    