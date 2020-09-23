'''
6. WAP to make a grocery list consisting of items - chocolate, milk, cereal and print it. 
'''

groceries = []

while True:
    item = input("Enter a grocery item:" )

    if item=='': break
    
    groceries.append(item)

print(groceries)

'''
OUTPUT:

Enter a grocery item:milk
Enter a grocery item:chocolate
Enter a grocery item:cereal
Enter a grocery item:daal
Enter a grocery item:chana
Enter a grocery item:
['milk', 'chocolate', 'cereal', 'daal', 'chana']
'''
