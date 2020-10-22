# Problem statement in description

sentence = input()
inp = input().lower().split()

map = {}
for s in sentence:
    s = s.lower()
    for i in inp:
        if i in s:
            map[s] = map.get(s,0) + s.count(i)

#print(map)

result = sorted(map.items(), key=lambda x : (-x[1],x[0]))

for i in result:
    print(i[0])

'''
Sentence: ["This is good", "Python is good", "Python is not python snake"]

Input: 
python is

Output:
1. python is not python snake
2. python is good
3. this is good
'''
