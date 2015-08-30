from math import *

def dot(a, b):
    if len(a) != len(b):
        return Null
    r = 0
    for i in range(len(a)):
        r = r + a[i]*b[i]
    return r

if __name__ == '__main__':
    a = input("a = ")
    b = input("b = ")
    print(dot(a,b))
