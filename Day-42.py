## 49.About Array:

# Create an array (list)
my_array = [1, 2, 3, 4, 5]

# Access elements of the array
print("Array elements:")
for element in my_array:
    print(element)

# Calculate the length of the array
array_length = len(my_array)
print(f"Length of the array: {array_length}")

# Accessing elements by index
index = 2
element_at_index = my_array[index]
print(f"Element at index {index}: {element_at_index}")

# Modify elements of the array
my_array[1] = 10
print("Modified array:")
print(my_array)

# Add an element to the end of the array
my_array.append(6)
print("Array after appending 6:")
print(my_array)

# Remove an element by value
value_to_remove = 4
if value_to_remove in my_array:
    my_array.remove(value_to_remove)
    print(f"Array after removing {value_to_remove}:")
    print(my_array)
else:
    print(f"{value_to_remove} not found in the array.")

# Sort the array
my_array.sort()
print("Sorted array:")
print(my_array)

# Reverse the array
my_array.reverse()
print("Reversed array:")
print(my_array)
