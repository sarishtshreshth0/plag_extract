#from collections import deque,defaultdict
printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 10**18
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

n = inn()
s = ins()
l = r = lv = rv = 0
for i in range(n):
    if s[i]=='(':
        l += 1
    elif l>0:
        l -= 1
    else:
        rv += 1
for i in range(n-1,-1,-1):
    if s[i]==')':
        r += 1
    elif r>0:
        r -= 1
    else:
        lv += 1
print('('*rv+s+')'*lv)
