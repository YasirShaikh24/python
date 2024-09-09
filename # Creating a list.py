# Creating a list
my_list = [1, 2, 3, 4, 5]

# Applying various methods
my_list.insert(2, 6)  # Inserting 6 at index 2
print(f"After insert(2, 6): {my_list}")

my_list.remove(3)  # Removing the element 3
print(f"After remove(3): {my_list}")

my_list.append(6)  # Appending 6 at the end of the list
print(f"After append(6): {my_list}")

length = len(my_list)  # Getting the length of the list
print(f"Length of the list: {length}")

popped_element = my_list.pop()  # Popping the last element
print(f"Popped element: {popped_element}")
print(f"After pop(): {my_list}")

my_list.clear()  # Clearing the list
print(f"After clear(): {my_list}")
