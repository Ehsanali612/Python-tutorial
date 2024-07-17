# class
'''Class is blue print for creating objects '''
# like thIS 
'''class student:
    name='Ehsan Ali'''
# Creating objects(Instance)
'''s1=student
print(s1.name)'''

# 2
'''
class Dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        '''
        # These are instances of class Dog 
'''
    def title(self):
        return self.name.title()
    '''
my_dog=Dog("Willie",6)
print("My Dog is "+ my_dog.title()+".")
print("My Dog age is " + str(my_dog.age)+".")

# You can use class to represent many real-world situations
# The Car
class Car():
    def __init__(self,make ,model,year): 
        # initializing attribute to describe .a car
        self.make=make
        self.model=model
        self.year=year
    def get_descriptive_name(self):
        "return a neatly formatted descriptive name"
        long_name=str(self.year)+''+ self.model
        return long_name.title()
my_new_car=Car('audi','A4','2016')
print(my_new_car.get_descriptive_name)

# Setting a Default value for an attribute
'''
---> Every attribute in class needs an initial value is 0
or an empty string .
'''
 