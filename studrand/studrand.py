import random

def dups(n):
    return len(set(n)) < len(n)

def tikimybe(a, b):
    return sum(1 for i in range(b) if dups([random.randint(1, 365) for j in range(a)])) / b

print(tikimybe(23, 1000))
