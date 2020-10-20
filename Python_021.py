# Problem statement in description

def calc(a,b,opr):
    return eval(str(a)+opr+str(b))

a = int(input())
b = int(input())
opr = input()

print(calc(a,b,opr))
