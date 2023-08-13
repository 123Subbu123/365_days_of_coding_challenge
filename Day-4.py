##9.Implement a function that divides two numbers and handles division by zero.
def div(num,den):
    try:
        return num/den
    except ZeroDivisionError:
        return "Denominator should be non zero"
print(div(6,0))
print(div(8,9))

##10.Write a program to remove duplicates from a list using a set.
list1=[3,9,7,5,9,4,4,9,6,3]
print("The original list is:"+str(list1))
list1=list(set(list1))
print("The list after removing duplicates:"+str(list1))

