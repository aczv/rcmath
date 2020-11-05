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

print (pastumti_zodi("Rugile",6))


