# a. Create a string called "something" with the value "Completely Different"
something = "Completely Different"

# b. Print all the properties and methods of the string.
print(dir(something))

# c. Use a string method to count the number of times the character "t" is present in the string.
count_t = something.count('t')
print("Number of 't' present:", count_t)

# d. Use a string method to find the first position of the sub-string "plete" in the string.
position = something.find('plete')
print("Position of 'plete':", position)

# e. Use a string method to split the string by the character "e".
split_something = something.split('e')
print("Split by 'e':", split_something)

# f. Create a new string ("thing2") that replaces the word "Different" with "Silly".
thing2 = something.replace('Different', 'Silly')
print("New string:", thing2)

# g. Try to assign the letter "B" to the first character of the string "something" using: something[0] = "B".
# This causes an error because strings in Python are immutable, meaning you cannot change their characters after they are created.
# You would need to create a new string with the desired change instead.
