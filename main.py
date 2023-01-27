print("-----Write your code below this line 👇-----")
print("Hello World!")

print('-----using the backslash n-----')
print("Hello World!\nHello World!\nHello World!")

print('-------Concatenate------')
print("Hello" + " Angela")
print('---or---')
print("Hello" + " " +"Angela")
print('---or---')
print("Hello " + "Angela")

'''
Errors in python: Syntax error, indentation error,
'''

print("-------Ask the user input-------instead of print it is input")
input("What is your name? ")

print("-------print and the input prompt nested / concatenate -------")
print("Hello " + input("What is your name? "))

# ctrl + forward / helps to commment the selected lines of code 

# print the len of a word without a variable 
print(len(input("Name of your pet: ")))
# now get the length of the word using varibles 
name = input("What is your name? ")
length = len(name)
print(length) 