file_name = 'pi_digits.txt'
with open(file_name) as file_object :
    lines = file_object.readlines()
# the ---> .readlines()---> methode read line from file and stores it to a list
for line in lines:
    print(line.strip())
# There we simply loop it so the conents match excatly to the original file
# Working with files contents
pi_string = ''
# Ther we creat a string to store data of string 
for line in lines:
    pi_string+=line.rstrip()
print(pi_string)
print(len(pi_string))
