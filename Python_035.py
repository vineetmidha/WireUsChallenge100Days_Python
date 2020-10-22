# Problem statement in description

temp = int(input("Enter temperature: "))
unit = input("(1) Celsius (2) Fahrenheit: ")

if unit == '1':
    c = temp
    f = int(c*9/5+32)
    print(f"{c} C is {f} in Fahrenheit")
elif unit == '2':
    f = temp
    c = int((f-32)/9*5)
    print(f"{f} F is {c} in Celsius")
else:
    print("Invalid unit")

'''

Enter temperature: 60
(1) Celsius (2) Fahrenheit: 1
60 C is 140 in Fahrenheit

Enter temperature: 45
(1) Celsius (2) Fahrenheit: 2
45 F is 7 in Celsius

'''
