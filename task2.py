#!python3

"""
Create a variable that contains an empy list.
Ask a user to enter 5 words.  Add the words into the list.
Print the list
inputs:
string 
string
string
string
string

outputs:
string

example:
Enter a word: apple
Enter a word: worm
Enter a word: dollar
Enter a word: shingle
Enter a word: virus

['apple', 'worm', 'dollar', 'shingle', 'virus']
"""

a = str(input("Please enter word "))
b = str(input("Please enter word "))
c = str(input("Please enter word "))
d = str(input("Please enter word "))
e = str(input("Please enter word "))

wordlist = [a,b,c,d,e]
print(wordlist)