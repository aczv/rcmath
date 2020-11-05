def pastumti_zodi (a, k):
    s = ""
    for x in a:
        t = ord(x.lower()) + k
        if t > ord('z'):
            t -= 26
        s += chr(t).upper() if x.isupper() else chr(t)
    return s

if __name__ == "__main__":
    print(pastumti_zodi("Rugile", 6))
