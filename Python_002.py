# Accept a number and count its digits

n = int(input("Enter a number: "))
c = 0

while n:
    n //= 10
    c += 1

print("Count of digits:", c)

'''
Output:

Enter a number: 24578
Count of digits: 5
'''
