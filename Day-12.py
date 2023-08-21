## 20.PYTHON PROGRAM TO GENERATE PASWORD.
import random
passlen=int(input("Enter the length of password:"))
s="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p="".join(random.sample(s,passlen))
print(p)
