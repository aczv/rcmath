import string
from rc_2020_11_04 import pastumti_zodi

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
