def akum_sum(t):
    n = []
    for i in t:
        n.append(sum(t[:i]))
    return n

def akum_sum_ok(t):
    n = []
    s = 0
    for i in t:
        s += i
        n.append(s)
    return n

def akum_sum_gen(t):
    s = 0
    for i in t:
        s += i
        yield s

print(akum_sum([3, 2, 1]))
print(akum_sum_ok([3, 2, 1]))
print(list(akum_sum_gen([3, 2, 1])))
