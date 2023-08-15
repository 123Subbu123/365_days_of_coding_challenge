##13.Create a list of numbers and sort them using a lambda function as the sorting key.
numbers=[3,5,9,2,4,7]
print("Original:",numbers)
numbers.sort(key=lambda x:x)
print("Sorted:",numbers)

##14.Write a generator function to generate the sequence of prime numbers.
def is_prime_num(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i++0:
            return False
    return True
def prime_numbers(start,end):
    for num in range (start,end+1):
        if is_prime_num(num):
            yield num

start=int(input("Input the satrting number:"))
end=int(input("Input the ending number:"))

prime_gen=prime_numbers(start,end)
print("Prime numbers between",start,"and",end,"are:")
for prime in prime_gen:
    print(prime,end=",")
