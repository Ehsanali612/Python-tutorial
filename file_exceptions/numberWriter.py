# Using json.dump and json.load 

# json.dump ---> Is use to store a set of numbers
# --->It takes two arguments : a piece of data to 
# store and a file object it can use to store the data. Here’s how you can use 
# json.dump() to store a list of numbers


#  json.load--->  other reads back to the memory

import json
numbers = [ 2,3,4,55,5,6,7,8]
filename = 'numbers.json'
# the json indicatted that file created ini the jso formate 
with open(filename,'w') as file_object:
    json.dump(numbers,file_object)
