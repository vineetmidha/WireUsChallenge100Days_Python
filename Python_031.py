# Problem statement in description

def is_palin(n):
    return str(n) == str(n)[::-1]

t = int(input("Test Cases: "))

for _ in range(t):
    n = int(input("Input: "))

    while True:
        n += 1
        if is_palin(n):
            print("Output:", n)
            break
            
'''

Test cases: 3
Input: 10
Output: 11
Input: 20
Output: 22
Input: 44
Output: 55

'''
