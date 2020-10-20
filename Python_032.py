# Problem statement in description

s = input("Enter string: ")

score = 0

for i in s:
    if i in 'AEIOUaeiou':
        score += 5
    elif i in 'friends':
        score += 10
    else:
        score += 1

if score > 100:
    print("Congratulations you are a best friend")
else:
    print(score)
    
'''
Enter string: akdjsf;lajsdkf;asdkf
Congratulations you are a best friend

Enter string: hum aapkay hain kaun
70
'''
