##11.Implement a recursive function to calculate the nth term of the Fibonacci Series.
def Fibonnaci_Series(n):
    if n<0:
        print("Incorrect Input")
    elif n==0:
        return(0)
    elif n==1:
        return(1)
    else:
        return(Fibonnaci_Series(n-1)+Fibonnaci_Series(n-2))
print("12th element of Fibonnaci Series:",Fibonnaci_Series(12))

##12.Write a Program that demonstrates the use of multithreading in python.
import threading
def print_cube(n):
    print("Cube:{}".format(n*n*n))
def print_square(n):
    print("square:{}".format(n*n))
if __name__ =="__main__":
    t1=threading.Thread(target=print_square,args=(10,))
    t2=threading.Thread(target=print_cube,args=(10,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Done!")