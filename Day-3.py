##6.Implement a function that finds the largest element in an array of numbers.
import numpy as np
arr=[345,23,674,888888,23,11,87,98,6382726]
max=arr[0]
for i in range(0,len(arr)):
    if (arr[i]>max):
        max=arr[i]
print("largest element in the array is :",str(max))

##7.Create an object representing a person with properties like name,age,and address.
class person:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
p1=person("Bandita",39,"BHUBANESWAR")
print(p1.name)
print(p1.age)
print(p1.address)


##8.Write a function that reverses a given string
def reverse(str):
    return str[::-1]
string=reverse("Subhalaxmi")
    
print(string)
    
    
