def pastumti_zodi (a, k):
    s = ""
    for x in a:
        if x.isupper():
            x = x.lower()
            t = ord(x) + k
            if t > ord('z'):
                t -= 26
            s += chr(t).upper()
        else:
            t = ord(x) + k
            if t > ord('z'):
                t -= 26
            s += chr(t)
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
