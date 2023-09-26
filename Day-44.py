## 51. Create an empty dictionary to store student information
student_dict = {}

# Add students to the dictionary
student_dict["Alice"] = {"age": 18, "grade": "A"}
student_dict["Bob"] = {"age": 19, "grade": "B"}
student_dict["Charlie"] = {"age": 17, "grade": "C"}

# Accessing dictionary values
print("Student Information:")
print("Alice's Age:", student_dict["Alice"]["age"])
print("Bob's Grade:", student_dict["Bob"]["grade"])

# Modifying dictionary values
student_dict["Charlie"]["age"] = 18  # Charlie had a birthday
print("Charlie's Updated Age:", student_dict["Charlie"]["age"])

# Checking if a key exists in the dictionary
if "David" in student_dict:
    print("David's Information:", student_dict["David"])
else:
    print("David is not in the dictionary.")

# Removing a student from the dictionary
if "Bob" in student_dict:
    del student_dict["Bob"]
    print("Removed Bob from the dictionary.")

# Iterating through the dictionary
print("\nAll Students:")
for name, info in student_dict.items():
    print(f"Name: {name}, Age: {info['age']}, Grade: {info['grade']}")
