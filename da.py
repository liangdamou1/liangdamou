def da(x,y):
    if x > y:
        return x
    elif x < y:
        return y
    else:
        return x

def dd(a,b):
    if a > b:
        c = da(2000,3000)+1
        return c
    elif a < b:
        c =  da(3000,5000)+1
        return c
    else:
        c= da(3000,6000)+3
        return c

def db():
    k=dd(4,6)
    print (k)

db()