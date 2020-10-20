# Problem statement in description

class calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return eval(str(self.a) + "+" + str(self.b))

calc = calculator(10,20)
print(calc.add())
calc = calculator(100,200)
print(calc.add())

'''
Output:

30
300

'''
