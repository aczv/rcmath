def apgrezimas(a, b):
    aa = str(a)
    bb = str(b)[::-1]
    return aa == bb

def apgrezimas2(a, b):
    aa = str(a).zfill(2)
    bb = str(b)[::-1].zfill(2)
    return aa == bb

def metai(f, nn):
    """
    a - dukros amzius
    b - mamos amzius
    x - skirtumas
    """
    for x in range(1, 100):
        n = []

        for a in range(1, 100):
            b = a + x
            if f(a, b):
                n.append(a)

        if len(n) == nn:
            # print('Man metu: %s' % n[5])
            print(nn, x, [(i, i + x) for i in n])

for n in range(1, 10):
    metai(apgrezimas, n)
    metai(apgrezimas2, n)
