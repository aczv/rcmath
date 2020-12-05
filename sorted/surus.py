def  yra_surusiuotas(t):
    return sorted(t) is t

def  yra_surusiuotas2(t):
    for i in range(1, len(t)):
        if t[i - 1] > t[i]:
            return False
    return True

def yra_surusiuotas3(t):
    k = 0
    for i in range(len(t)):
        if sorted(t)[i] is not t[i]:
            k += 1
    return k is 0

m = [
    [1, 2, 3],
    [2, 1, 3],
    [1],
    [],
]

def method4(t):
    return all(t[i] <= t[i + 1] for i in range(len(t) - 1))

for t in m:
    print(t, yra_surusiuotas(t), yra_surusiuotas2(t), yra_surusiuotas3(t), method4(t))
