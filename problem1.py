#!python3
"""
Print the list named "people"
Ask the user to enter a word from the list
Ask the user to enter another word
Replace the first word with the second word.

inputs:
string
string

outputs:
list

example:
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
Choose a person from the list to replace:Rick
Enter the replacement:Dan
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Dan']

"""
people = ['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
print(people)
y = (input("Please enter name to remove ")).strip()
try:
    people.index(y)
except:
    exit()
num = int(people.index(y))
x = (input("Please enter name to add "))
people.remove(y)
people.insert(num, x)


print(people)
