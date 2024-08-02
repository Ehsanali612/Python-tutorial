'''Let’s pull in the text of Alice in Wonderland and try to count the number 
of words in the text. We’ll use the string method split(), which can build a 
list of words from a string. Here’s what split() does with a string containing 
just the title "Alice in Wonderland":'''

title = "Aice in wonderland "
words = title.split()
"""THere it will change a string into a list and the count by len fun"""
print(len(words))
# Splits methode seperate a string into parts wherever it finds a ()
# space and stores all the parts of the string in  list
