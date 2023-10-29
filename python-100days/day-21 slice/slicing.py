import random
reverse = "Hello"[::-1]
odd = "Hello"[::2]
even = "Hello"[1::2]
rand = random.choices('Hello')

print(reverse, even, odd, rand)
