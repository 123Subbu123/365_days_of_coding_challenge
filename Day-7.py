##15.Use map, filter, and reduce functions to manipulate a list of numbers
#map() function:
base=[2,4,6,8,10]
power=[1,2,3,4,5]
answer=list(map(pow,base,power))
print("Answer:",answer)

#filter() function:
from math import sqrt
data=[0,1,4,6,8,9,10,12,16,81,23,36]
def isPerfectSqr(i):
    return sqrt(i).is_integer()
answer=list(filter(isPerfectSqr,data))
print("Answer:",answer)

#reduce() function:
from functools import reduce
def add(a,b):
    return a+b
num_list=[1,2,3,4,5,6,7,8,9,10]
sum=reduce(add,num_list)
print(f"Sum of the integers of num_list:{sum}")
sum=reduce(add,num_list,10)
print(f"Sum of the integers of num_list with initial value 10:{sum}")
