# Random Password Generator

import random
import string

charValues = string.ascii_letters +string.digits +string.punctuation
finalPass =""
length = int(input("Enter the password length :"))

#while len(finalPass) <length:
#    finalPass = finalPass+ random.choice(charValues)

print("your random password is:",finalPass)
#list Comprehension [funciton for i in range (n)]

Password="".join([random.choice(charValues) for i in range(length)])

print("your random password is:",Password)