# Similar like small files we can read large files without any problem
# we will print a we want to print digits like here we will print and other remaning will be 
#  print shortly 
# like
file_name = 'million.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()
string=''
for line in lines:
    string += line.strip()
print(string[:20] + "...")
print(len(string))
# trying some logic
birthday =input('PLS enter ')
if birthday in string:
    print('Your luckiest person in universe ')
else:
    print('You are un-lucky in your famaliy')