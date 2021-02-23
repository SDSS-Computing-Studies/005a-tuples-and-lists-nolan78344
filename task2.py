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
wordlist = []

a = str(input("Please enter word ")).strip()
b = str(input("Please enter word ")).strip()
c = str(input("Please enter word ")).strip()
d = str(input("Please enter word ")).strip()
e = str(input("Please enter word ")).strip()

wordlist.append(a)
wordlist.append(b)
wordlist.append(c)
wordlist.append(d)
wordlist.append(e)
print(wordlist)