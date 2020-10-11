# Problem statement in description

a = [2, 5, 12, 13, 25, 43, 40]

print(a)

for i in range(len(a)//2):
    a[i],a[-(i+1)] = a[-(i+1)],a[i]

print(a)

'''

Original: [2, 5, 12, 13, 25, 43, 40]
Reversed: [40, 43, 25, 13, 12, 5, 2]

'''
