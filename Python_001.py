# WAP to identify the data types of different inputs given by the user.

x = eval(input("Give some input: "))
print(type(x))

'''
Output:
>>> x = eval(input("Enter input:"))
Enter input:2
>>> type(x)
<class 'int'>

>>> x = eval(input("Enter input:"))
Enter input:1.2
>>> type(x)
<class 'float'>

>>> x = eval(input("Enter input:"))
Enter input:5j
>>> type(x)
<class 'complex'>

>>> x = eval(input("Enter input:"))
Enter input:'abc'
>>> type(x)
<class 'str'>

>>> x = eval(input("Enter input:"))
Enter input:[1,2]
>>> 
>>> type(x)
<class 'list'>

>>> x = eval(input("Enter input:"))
Enter input:(1,0)
>>> 
>>> type(x)
<class 'tuple'>

>>> x = eval(input("Enter input:"))
Enter input:{1:1,2:2}
>>> 
>>> type(x)
<class 'dict'>

>>> x = eval(input("Enter input:"))
Enter input:{1,2}
>>> type(x)
<class 'set'>

>>> x = eval(input("Enter input:"))
Enter input:b'abc'
>>> type(x)
<class 'bytes'>
'''
