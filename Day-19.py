## 27.Function to find permutations of a given string
from itertools import permutations
def allPermutations(str):
    permList=permutations(str)
    for perm in list(permList):
        print("".join(perm))

if __name__=="__main__":
    str="ABC"
    allPermutations(str)