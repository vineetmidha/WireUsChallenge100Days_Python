# Problem statement in description

def perfectSquares(start, end):
    for i in range(start, end+1):
        if i**0.5 == int(i**0.5):
            print(i, end=' ')

start = 10
end = 200
perfectSquares(start, end)

''' 
Output: 16 25 36 49 64 81 100 121 144 169 196 
'''
