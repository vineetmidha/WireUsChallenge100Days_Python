# 48.	WAP to generate a 2D array containing 4 rows with 5 random numbers in each row.

import random

array2d = []

for _ in range(4):
    row = [random.randint(100,200) for _ in range(5)]
    array2d.append(row)

for row in array2d:
    print(row)

'''

[147, 194, 199, 148, 139]
[123, 113, 119, 180, 155]
[184, 124, 122, 134, 153]
[128, 187, 110, 168, 191]

'''
