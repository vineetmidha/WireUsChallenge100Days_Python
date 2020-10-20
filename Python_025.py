# Problem statement in description

s = input("Enter a string: ")

vowels = {}

for v in s:
    if v in 'aeiouAEIOU':
        vowels[v.lower()] = vowels.get(v.lower(), 0) + 1

print(vowels)

'''
Enter a string: this is a vowel STRING WITH VOWELS
{'i': 4, 'a': 1, 'o': 2, 'e': 2}
'''
