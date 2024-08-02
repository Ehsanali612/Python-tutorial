'''
with open('pi_digits.txt','r') as file_object :
    contents = file_object.read()
    print(contents.rstrip())
'''
    # rstrip()--> is used bcz we wnat to remove extra blank spacces on  right side
'''But some times the file is not in the directory in which our code is 
so we have also solution for that like below code '''
'''
with open ('Demo_file\pi_digits.txt') as file_object :

    # You should use --> \ (back slash )
    # insted of ---> / (forward slash)
contents = file_object.read()
print(contents)
'''
#  NOte : it only reades a file inside the file that we coding in 

'''For more accurate in other file in window we use this '''
# And on windows it look like this 
'''
file_path = 'C:\Users\ehmatthes\other_files\text_files\filename.txt'
with open(file_path) as file_object:
'''
# Windows systems will sometimes interpret forward slashes in file paths correctly. If 
# you’re using Windows and you’re not getting the results you expect, make sure you try 
# using backslashes
# printing file line by line 
file_name = 'pi_digits.txt'
with open(file_name) as file_object:
    for line in file_object:
        print(line)


