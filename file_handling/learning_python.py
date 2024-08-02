'''file = 'learningPython.txt'
with open(file,'r') as files_name:
    print(files_name.read())
'''
#  reading files through for loops 
'''file = 'learningPython.txt'
with open(file,'r') as files_name:
    for files in files_name :
        print(files)
'''

# Reading files line by line 
'''file = 'learningPython.txt'
with open(file,'r') as files_name:
    contets =files_name.readlines()
    print(contets)
'''
# we can also replace lines or word in a string  like this 
message = 'Hello bunty how are you :'
message.replace('Hello' , 'Ehsan')
print(message)