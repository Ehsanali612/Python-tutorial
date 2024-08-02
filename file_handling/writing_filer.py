# Write to an empty file just like read a file 
file_name = 'Programing.txt'

with open(file_name,'w') as file_object:
    file_object.write('I love programing.')
    file_object.write('I love You Ehsan bhi')
# You  can open a file in read mode('r') ,write mode ('w'), and ,append mode ('a')
# or alternativelt you can chose ('r') , that have all these characteristics at once
# When you open this file you will see that its in file
''' Python only stores texts in a string , so for that you have change into the string '''
# you can also add mutilple lines of texts like this 
# You can also added \n line also
# like this
# file_object.write("I love creating new games.\n")
