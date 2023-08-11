##4.Create a program that generates the Fibonacci sequence up to a certain number of terms
def Fibonacci(n):
    if n<=0:
        print("Incorrect Input")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
print(Fibonacci(10))
##5.Write a function that finds the largest element in an array of numbers.
arr = [10, 89, 9, 56, 4, 80, 8]
print (max(arr))