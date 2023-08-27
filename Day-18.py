##26.Check if given array is Monotonic.
def isMonotonic(A):
    x,y=[],[]
    x.extend(A)
    y.extend(A)
    x.sort()
    y.sort(reverse=True)
    if(x==A or y==A):
        return True
    return False
A=[6,5,4,4]
print(isMonotonic(A))
