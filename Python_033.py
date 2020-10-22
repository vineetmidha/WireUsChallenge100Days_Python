# Problem statement in description

import re

# abc@yahoo.com vineet@gmail.com codxcrypt@gmail.com xyz@hotmail.com

s = input("Enter a string: ")

gmails = re.findall(r'[\w\.-]+@gmail.com+', s)

f = open("allgmails.txt", "w")

for email in gmails:
    f.write(email + "\n")
    
f.close()

f = open("allgmails.txt")

for email in f:
    print(email, end="")
    
f.close()

'''

Enter a string: abc@yahoo.com vineet@gmail.com codxcrypt@gmail.com xyz@hotmail.com

vineet@gmail.com
codxcrypt@gmail.com

'''
