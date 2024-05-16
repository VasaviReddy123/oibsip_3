import string
import random
lower=string.ascii_lowercase
upper=string.ascii_uppercase
digits=string.digits
symbols=string.punctuation
while True:
    passwordlength=int(input("Enter length of the the password:"))
    
    if passwordlength<6:
        print("password length should be more than 6.")
        continue
    else: 
        break
c=lower+upper+digits+symbols
password=""
for i in range(passwordlength):
    password+=random.choice(c)
print("The random password generated with the given length is: ",password)