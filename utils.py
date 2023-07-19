def l2dtostr(l2d: list(list()), fd:str()=" ", sd:str()="!"):
    return fd.join([sd.join(a) for a in l2d])

def strtol2d(str: str(), fd:str()=" ", sd:str()="!"):
    return [a.split(sd) for a in str.split(fd)]

foo = [["a", "b"], ["c", "d"]]
#t = ' '.join(['!'.join(a) for a in foo])
t = l2dtostr(foo)
print(t)
#m = [a.split('!') for a in t.split(' ')]
m = strtol2d(t)
print(m, m==foo)