def tripleend(s):
    l = len(s)
    w=s[l-2:]
    return w+w+w

print(tripleend("hello"))
print(tripleend("hi"))
print(tripleend("goodbye"))
