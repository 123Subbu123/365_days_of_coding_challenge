## 50.About list
# Creating a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements of the list
print("Element at index 0:", my_list[0])  # Accessing the first element
print("Element at index 2:", my_list[2])  # Accessing the third element

# Modifying elements of the list
my_list[1] = 10  # Modifying the second element
print("Modified list:", my_list)

# Finding the length of the list
list_length = len(my_list)
print("Length of the list:", list_length)

# Adding an element to the end of the list
my_list.append(6)
print("List after adding an element:", my_list)

# Removing an element by value
if 3 in my_list:
    my_list.remove(3)
print("List after removing element 3:", my_list)

# Inserting an element at a specific index
my_list.insert(2, 7)  # Inserting 7 at index 2
print("List after inserting 7 at index 2:", my_list)

# Iterating through the list
print("Iterating through the list:")
for element in my_list:
    print(element)

# Slicing the list
sliced_list = my_list[1:4]  # Extracting elements from index 1 to 3
print("Sliced list:", sliced_list)

# Sorting the list
my_list.sort()
print("Sorted list:", my_list)

# Reversing the list
my_list.reverse()
print("Reversed list:", my_list)
