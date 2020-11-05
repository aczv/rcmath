def pastumti_zodi (a, k):
    i=0
    s = ""
    while i<len(a):
        if a[i].isupper():
            a[i].lower()
            t = ord(a[i]) + k
            if t > ord('z') + 1:
                t -= 26
            s += chr(t).upper()
        else:
            t = ord(a[i]) + k
            if t > ord('z'):
                t -= 26
            s += chr(t)
        i+=1
    return s

import string

az = string.ascii_lowercase
AZ = string.ascii_uppercase
m = [
    ("Rugile", 6),
    ("Rugile", 1),
    ("Rugile", 0),
    (az, 0),
    (az, 1),
    (az, 25),
    (AZ, 0),
    (AZ, 1),
    (AZ, 25),
]

for x in m:
    print (pastumti_zodi(*x), x)
