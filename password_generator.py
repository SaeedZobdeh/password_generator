import random
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbol = "[]()*:;/.-_#@%^&!?"
all = lower + upper + numbers + symbol 
length = 15 
password = "".join(random.sample(all,length))
print("password is : " + password )  