import math
def py():
    print("Yes")
def pn():
    print("No")
def iin():
    x = int(input())
    return x

neko = 0
nya = 0
nuko = 0
h,w = map(int,input().split())
neko = h%2
nya = w%2
nuko = h * w /2
if neko + nya == 2:
    nuko = nuko + 1
if (h == 1)or(w == 1):
    nuko = 1
print(int(nuko))