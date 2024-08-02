'''Failing Silently
In the previous example, we informed our users that one of the files 
was unavailable. But you don’t need to report every exception you catch. 
Sometimes you’ll want the program to fail silently when an exception occurs 
and continue on as if nothing happened. To make a program fail silently, you 
write a try block as usual, but you explicitly tell Python to do nothing in the 
except block. Python has a pass statement that tells it to do nothing in a block'''

# def countWords(filename):
#     try:
#         with open(filename) as f_obj:
#             contents = f_obj.read() 

#     except FileNotFoundError:
#         msg = "Sorry, the file " + filename + " does not exist."
#         print(msg)
#         pass

#     else:
#         # Count approximate number of words in the file.
#         words = contents.split()
#         num_words = len(words)
#         print("The file " + filename + " has about " + str(num_words) + 
#         " words.")

#     filename = 'alice.txt'
#     countWords(filename)



