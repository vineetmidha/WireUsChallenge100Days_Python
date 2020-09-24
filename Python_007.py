'''
WAP to generate and print a dictionary that contains 1 to n numbers as keys
and the value is the square of the number. 
'''

n=int(input("Enter a  number: "))
d = {x:x*x for x in range(1,n+1)}
print(d)

'''
Output:

Enter a  number: 10
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

'''
