## 31. Python Program for Find remainder of array multiplication divided by n.
import math
def find_remainder(arr,n):
    log_sum=0
    for i in arr:
        log_sum+=math.log10(i)

    remainder=int(pow(10,log_sum))%n
    return remainder

arr=[100,10,5,25,35,14]
ele=11
rem=find_remainder(arr,ele)
print(rem)