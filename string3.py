def rotate(s):
    l=len(s)
    w=s[0:2]
    p=s[2:l]
    return p+w
print(rotate("hello"))
print(rotate("java"))
print(rotate("coding"))
