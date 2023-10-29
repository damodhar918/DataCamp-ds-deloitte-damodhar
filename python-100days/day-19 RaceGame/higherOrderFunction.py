def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def product(a,b):
    return a * b
def divide(a,b):
    return a / b


def calculator(a,b,func):
    return func(a,b)


a, b = map(int,input('Enter the numbers(a, b): ').split())
results = calculator(a, b ,divide)
print(results)