
# Code 1
car='bugatti'
print("is car=='bugatti'\b i predict true ")
print(car=='bugatti')
print("\n is car==suzuki \b i predict false")
print(car=="suzuki")

#2
alien_color='Green'
if alien_color=='Green':
    print('You just earn 5 points ')
if alien_color!='Green':
    print("You just earn 10 points")
elif alien_color=='yellow':
    print('You just earn 10 points')
elif alien_color=='red':
    print('You just  earn 15 points ')
else:
    print('Player earn zero')

# 3
requested_gradients=['peeper','mango','carrot']
for requested_gradient in requested_gradients:
    if requested_gradient=='mango':
        print('sorry the mango is not available')
    else:
        print('Finished making your Gradient')


# 4
userNames=['adan','ahmed','ehsan','ibrahim']
if 'admin' in userNames:
    print(f'Hello admin, would you like to see a status report?')
else:
    for others in userNames:
        print(f'Hello {others.title()}, thank you for logging in again.')

# 5

list=[1,2,3,4,5,6,7,8,9,10]
for lists in list:
    if lists:
        print(f'{lists}th')
    else:
        print('Thank You ! ')