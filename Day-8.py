##16.Write a function that validates whether an input string is a valid email address.
import re
regex=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
def check(email):
    if(re.fullmatch(regex,email)):
        print("Valid email")
    else:
        print("Invalid Email")
if __name__=="__main__":
    email="subhalaxmimallick149@gmail.com"
    check(email)
    email="21cseds043.subhalaxmimallick@giet.edu"
    check(email)
    email="ankita326.com"
    check(email)